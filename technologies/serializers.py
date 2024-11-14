from rest_framework import serializers
from .models import Technology, Tech_Type

class TechnologySerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    icon = serializers.ImageField()  # Explicitly specify as ImageField

    class Meta:
        model = Technology
        fields = ['id', 'name', 'icon', 'description', 'proficiency', 'type', 'created_at', 'updated_at']


    def get_type(self, obj):
        return obj.type.type_name if obj.type else None
