from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


class PersonListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


@api_view(["POST"])
@permission_classes([])
def register(request):
    data = request.data
    password = data.get("password")

    person = Person.objects.create(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
    )
    from django.contrib.auth import models as models_auth

    person.user = models_auth.User.objects.create_user(person.email, password=password)
    person.save()

    serializer = PersonSerializer(person)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
