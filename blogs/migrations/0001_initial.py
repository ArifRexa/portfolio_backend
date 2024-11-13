# Generated by Django 5.1.2 on 2024-11-07 18:49

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Category Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Tag Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Tag Slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('excerpt', models.TextField(blank=True, help_text='Short summary of the post', verbose_name='Excerpt')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published At')),
                ('is_published', models.BooleanField(default=False, verbose_name='Published')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='blog/covers/', verbose_name='Cover Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('categories', models.ManyToManyField(related_name='posts', to='blogs.category', verbose_name='Categories')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blogs.tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-published_at'],
            },
        ),
    ]