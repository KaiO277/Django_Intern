from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

  