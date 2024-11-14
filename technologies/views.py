from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Technology
from .serializers import TechnologySerializer

# List all technologies or create a new one
class TechnologyListCreateView(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            # Require authentication for POST requests
            return [permissions.IsAuthenticated()]
        # Allow any access for GET requests
        return [permissions.AllowAny()]

# Retrieve, update, or delete a specific technology by ID
class TechnologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure authentication for detail view operations
