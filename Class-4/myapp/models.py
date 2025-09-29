from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50,null=True)
    department=models.CharField(max_length=50,null=True)
    roll=models.IntegerField(max_length=50,null=True)
    Admission=models.DateField(null=True)

class TeacherModel(models.Model):
    name=models.CharField(max_length=50,null=True)
    department=models.CharField(max_length=50,null=True)
    roll=models.IntegerField(max_length=50,null=True)
    Admission=models.DateField(null=True)