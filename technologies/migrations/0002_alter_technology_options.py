# Generated by Django 5.1.2 on 2024-11-06 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name': 'Technology', 'verbose_name_plural': 'Technologies'},
        ),
    ]