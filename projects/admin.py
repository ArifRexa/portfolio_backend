from django.contrib import admin
from .models import Project, ProjectImage
from technologies.models import Technology
# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty image fields displayed by default

class TechnologyInline(admin.TabularInline):
    model = Project.technologies.through  # This allows you to access the through model for many-to-many relationships
    extra = 1  # Number of empty technology fields displayed by default

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, TechnologyInline]
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

# @admin.register(Technology)
# class TechnologyAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

admin.site.register(ProjectImage)