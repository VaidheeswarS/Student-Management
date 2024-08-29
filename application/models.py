from django.db import models

# Create your models here.

class students_info(models.Model):
    S_No=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=30,null=True)
    # Mid_Name=models.CharField(max_length=15,null=True)
    Last_Name=models.CharField(max_length=30,null=True)
    School=models.CharField(max_length=100,null=True)
    STD=models.CharField(max_length=7,null=True)
    section=models.CharField(max_length=2,null=True)
    D_O_B=models.DateField(null=True)
    Age=models.IntegerField(null=True)
    Parents_Phone_Number=models.BigIntegerField(null=True)
    Gender=models.CharField(max_length=10, null=True)
    Photo=models.ImageField(upload_to='photos/',null=True)
    Email_id=models.EmailField(max_length=50,null=True)
    Password=models.CharField(max_length=10,null=True)
