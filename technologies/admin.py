from django.contrib import admin
from .models import Technology
# Register your models here.

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'created_at', 'updated_at')  # Include proficiency in the display
    search_fields = ('name',)