from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

# Create your models here.



class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    avatar = models.ImageField(upload_to='images/avatar/', null=True, blank=True)
    document_file = models.FileField(upload_to='documents/',null=True, blank=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

class studentProfile(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    student_profile = models.ForeignKey(student, on_delete=models.CASCADE, related_name='student_profiles')

    def __str__(self):
        return f"Profile of {self.student.name}"