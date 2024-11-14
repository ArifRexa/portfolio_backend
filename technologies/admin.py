from django.contrib import admin
from .models import Technology, Tech_Type
# Register your models here.

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'created_at', 'updated_at')  # Include proficiency in the display
    search_fields = ('name',)


@admin.register(Tech_Type)
class TechnologyTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'description', 'created_at', 'updated_at')
    search_fields = ('type_name',)
    list_display_links = ('type_name',)
    list_filter = ('type_name',)
    # list_editable = ('description',)
    # exclude = ('slug',)
    # list_per_page = 25
    # list_max_show_all = 100
    # list_select_related = True