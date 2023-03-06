from django.contrib import admin
from .models import Student,Master,Task,StudentAnswer

# Register your models here.
mymodels = [Student,Master,Task,StudentAnswer]
admin.site.register(mymodels)