from django.db import models

# Create your models here.
class Demo(models.Model):
    mail=models.EmailField(max_length=100)
    password=models.CharField(max_length=40)


class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=50)