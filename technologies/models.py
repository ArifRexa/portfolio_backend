from django.db import models

# Create your models here.


class Tech_Type(models.Model):
    type_name = models.CharField(max_length=100, help_text="Name of the technology type")
    description = models.TextField(blank=True, help_text="Brief description of the technology type")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the technology type entry was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the technology type entry was last updated")

    def __str__(self):
        return self.type_name
    
    class Meta:
        verbose_name = "Technology Type"
        verbose_name_plural = "Technology Types"
    

class Technology(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the technology")
    icon = models.ImageField(upload_to='technology_icons/', help_text="Icon or image representing the technology")
    description = models.TextField(blank=True, help_text="Brief description of the technology")
    proficiency = models.IntegerField(default=0, help_text="Expertise percentage (0 to 100)")
    type = models.ForeignKey(Tech_Type, on_delete=models.SET_NULL, null=True, blank=True, help_text="Type of the technology")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the technology entry was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the technology entry was last updated")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
