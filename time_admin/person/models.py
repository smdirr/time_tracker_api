from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
