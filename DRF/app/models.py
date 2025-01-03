from django.db import models

class stud(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.CharField(max_length=30)
# Create your models here.
