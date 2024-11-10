from django.db import models
from technologies.models import Technology
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the project")
    description = models.TextField(help_text="Detailed description of the project")
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True, help_text="Technologies used in the project")
    thumbnail_image = models.ImageField(upload_to='project_images/', null=True, blank=True, help_text="Main image for the project")
    live_link = models.URLField(null=True, blank=True, help_text="Link to the live project, if available")
    github_link = models.URLField(null=True, blank=True, help_text="Link to the project's GitHub repository")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the project was added")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the project details were last updated")

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, help_text="Associated project for this image")
    image = models.ImageField(upload_to='project_images/', help_text="Additional image for the project")
    caption = models.CharField(max_length=200, null=True, blank=True, help_text="Optional caption for the image")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.project.title}"
    
# class Technology(models.Model):
#     name = models.CharField(max_length=100, help_text="Name of the technology")
#     icon = models.ImageField(upload_to='technology_icons/', help_text="Icon or image representing the technology")
    
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = "Technology"
#         verbose_name_plural = "Technologies"