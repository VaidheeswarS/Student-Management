# Generated by Django 5.0.6 on 2024-06-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students_info',
            fields=[
                ('S_No', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=30, null=True)),
                ('Mid_Name', models.CharField(max_length=15, null=True)),
                ('Last_Name', models.CharField(max_length=30, null=True)),
                ('School', models.CharField(max_length=100, null=True)),
                ('STD', models.CharField(max_length=7, null=True)),
                ('section', models.CharField(max_length=2, null=True)),
                ('D_O_B', models.DateField(null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Parents_Phone_Number', models.BigIntegerField(null=True)),
                ('Gender', models.CharField(max_length=10, null=True)),
                ('Email_id', models.EmailField(max_length=50, null=True)),
            ],
        ),
    ]
