from django.contrib import admin
from .models import Experience
# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_title', 'start_date', 'end_date', 'get_duration', 'created_at', 'updated_at')
    readonly_fields = ('get_duration',)
    search_fields = ('company_name', 'job_title')