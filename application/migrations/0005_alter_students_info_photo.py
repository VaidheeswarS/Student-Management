# Generated by Django 5.0.6 on 2024-06-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_remove_students_info_mid_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_info',
            name='Photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
