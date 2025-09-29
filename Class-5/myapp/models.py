from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=150,null=True)
    roll=models.IntegerField(null=True)
    department=models.CharField(max_length=100,null=True)

class CourseModel(models.Model):
    title=models.CharField(max_length=150,null=True)
    code=models.CharField(max_length=20,unique=True)
    credit=models.IntegerField(null=True)

class TeacherModel(models.Model):
    name=models.CharField(max_length=150,null=True)
    Designation=models.CharField(max_length=50,null=True)
    email=models.EmailField(unique=True,null=True)
