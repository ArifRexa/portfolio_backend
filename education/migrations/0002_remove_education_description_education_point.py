# Generated by Django 5.1.2 on 2024-11-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='description',
        ),
        migrations.AddField(
            model_name='education',
            name='point',
            field=models.FloatField(blank=True, help_text='Your point', null=True, verbose_name='Point'),
        ),
    ]
