from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Project, ProjectImage
from .serializers import ProjectSerializer, ProjectCreateUpdateSerializer, ProjectImageSerializer

# List all projects or create a new one
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateUpdateSerializer
        return ProjectSerializer

# Retrieve, update, or delete a specific project
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateUpdateSerializer

# List all images for a specific project or add a new image
class ProjectImageListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectImageSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return ProjectImage.objects.filter(project__id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(id=project_id)
        serializer.save(project=project)

# Retrieve, update, or delete a specific project image
class ProjectImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
