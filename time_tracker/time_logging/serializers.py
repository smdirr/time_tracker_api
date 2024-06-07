from rest_framework import serializers
from .models import Project, Task, TimeEntry


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"


class TimeEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeEntry
        fields = "__all__"
