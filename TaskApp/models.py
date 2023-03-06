from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=20,default="")
    password = models.CharField(max_length=20,default="")
    confirmpassword = models.CharField(max_length=20,default="")

class Master(models.Model):
    username = models.CharField(max_length=20,default="")
    password = models.CharField(max_length=20,default="")
    confirmpassword = models.CharField(max_length=20,default="")

class Task(models.Model):
    task = models.CharField(max_length=50,default="")
    result = models.CharField(max_length=10,default="")

class StudentAnswer(models.Model):
    username = models.CharField(max_length=20,default="")
    task = models.CharField(max_length=50,default="")
    answer = models.CharField(max_length=10,default="")
    result = models.CharField(max_length=10,default="")