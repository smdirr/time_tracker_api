from django.db import models
from person.models import Person


class Project(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Project {self.code} {self.name}"


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, null=False)
    active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Task {self.code} {self.name}"


class TimeEntry(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)  # 4.5 hours
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.person} - {self.date} - {self.hours_worked} hours"
