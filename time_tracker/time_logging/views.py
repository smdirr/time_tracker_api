from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task, Project, TimeEntry
from .serializers import TaskSerializer, ProjectSerializer, TimeEntrySerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TimeEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
