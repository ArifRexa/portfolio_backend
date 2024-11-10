from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution_name', 'degree', 'field_of_study', 'start_date',
                    'end_date', 'get_duration', 'point', 'created_at', 'updated_at')
    list_filter = ('institution_name', 'degree', 'field_of_study', 'start_date', 'end_date')
    search_fields = ('institution_name', 'degree', 'field_of_study', 'grade', 'point')
    readonly_fields = ('get_duration',)
