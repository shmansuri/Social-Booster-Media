from django.db import models


# Create your models here.

class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    course = models.CharField(max_length=20)
    
