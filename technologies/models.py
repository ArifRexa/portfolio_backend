from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the technology")
    icon = models.ImageField(upload_to='technology_icons/', help_text="Icon or image representing the technology")
    description = models.TextField(blank=True, help_text="Brief description of the technology")
    proficiency = models.IntegerField(default=0, help_text="Expertise percentage (0 to 100)")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the technology entry was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the technology entry was last updated")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
