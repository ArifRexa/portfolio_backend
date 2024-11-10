from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Tag, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'published_at', 'created_at', 'updated_at')
    list_filter = ('is_published', 'categories', 'tags', 'created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    filter_horizontal = ('categories', 'tags')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'content', 'excerpt', 'cover_image')
        }),
        ('Publishing Options', {
            'fields': ('is_published', 'published_at', 'categories', 'tags')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
