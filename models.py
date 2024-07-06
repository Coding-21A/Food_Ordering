from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    repassword=models.CharField(max_length=100)