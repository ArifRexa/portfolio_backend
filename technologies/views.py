from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Technology
from .serializers import TechnologySerializer

# List all technologies or create a new one
class TechnologyListCreateView(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

# Retrieve, update, or delete a specific technology by ID
class TechnologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
