from rest_framework import serializers
from .models import Technology

class TechnologySerializer(serializers.ModelSerializer):
    icon = serializers.ImageField()  # Explicitly specify as ImageField

    class Meta:
        model = Technology
        fields = ['id', 'name', 'icon', 'description', 'proficiency', 'created_at', 'updated_at']
