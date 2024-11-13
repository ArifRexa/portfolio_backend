# Generated by Django 5.1.2 on 2024-11-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the technology', max_length=100)),
                ('icon', models.ImageField(help_text='Icon or image representing the technology', upload_to='technology_icons/')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='technologies',
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(blank=True, help_text='Technologies used in the project', related_name='projects', to='projects.technology'),
        ),
    ]