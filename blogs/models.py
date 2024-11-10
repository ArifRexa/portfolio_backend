from django.db import models
from django.conf import settings
# Create your models here.
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Category Slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Tag Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Tag Slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    # author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Author",
        related_name="posts"
    )
    content = RichTextField(verbose_name="Content")
    # content = CKEditor5Field(verbose_name="Content")
    excerpt = models.TextField(verbose_name="Excerpt", blank=True, help_text="Short summary of the post")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Published At")
    is_published = models.BooleanField(default=False, verbose_name="Published")
    categories = models.ManyToManyField(Category, related_name="posts", verbose_name="Categories")
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True, verbose_name="Tags")
    cover_image = models.ImageField(upload_to='blog/covers/', blank=True, null=True, verbose_name="Cover Image")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published_at']
