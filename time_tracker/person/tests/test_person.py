from django.test import TestCase
from django.urls import reverse
from person.models import Person


class TestPerson(TestCase):

    def setUp(self) -> None:
        super().setUp()
        my_pass = "devtestlocal"
        data = {
            "first_name": "Thomas",
            "last_name": "Anderson",
            "email": "tand@mail.me",
            "password": f"{my_pass}",
        }
        self.user = self.client.post(reverse("user_register"), data)

        token = self.client.post(
            reverse("token_obtain_pair"),
            {"username": data.get("email"), "password": f"{my_pass}"},
        )
        self.access_token = token.json().get("access")

    def test_get_person(self):

        response = self.client.get(
            reverse("person-list-create"),
            headers={"Authorization": f"Bearer {self.access_token}"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["first_name"], "Thomas")
        self.assertEqual(response.json()[0]["email"], "tand@mail.me")

    def test_get_person_401(self):
        response = self.client.get(reverse("person-list-create"))
        self.assertEqual(response.status_code, 401)

    def test_get_persons(self):

        Person.objects.create(first_name="John", last_name="Doe", email="john@test.com")

        response = self.client.get(
            reverse("person-list-create"),
            headers={"Authorization": f"Bearer {self.access_token}"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[1]["email"], "john@test.com")

    def test_retrieve_person(self):

        my_person = Person.objects.create(
            first_name="Juan", last_name="Fangio", email="jf@test.com"
        )

        response = self.client.get(
            f"/api/v1/person/{my_person.id}/",
            follow=True,
            headers={"Authorization": f"Bearer {self.access_token}"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["email"], "jf@test.com")

    def test_str_person(self):

        person = Person.objects.create(
            first_name="John", last_name="Doe", email="john@test.com"
        )
        self.assertEqual(str(person), "Doe, John")
