from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
