# Generated by Django 5.0.6 on 2024-06-19 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_students_info_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students_info',
            name='Mid_Name',
        ),
    ]