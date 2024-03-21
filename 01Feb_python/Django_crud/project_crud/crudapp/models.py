from django.db import models
import os
from django.contrib.auth.models import User



# Create your models here.

class Student(models.Model):
    uname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    lang=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    img=models.ImageField(upload_to='images')
    
class User(models.Model):
    phoneno = models.CharField(max_length=50)