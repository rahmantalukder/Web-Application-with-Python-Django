from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name =models.CharField(max_length=100,null=True)
    department =models.CharField(max_length=100,null=True)
    city =models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)

    contact =models.CharField(max_length=100,null=True)
class TeacherModel(models.Model):
    name =models.CharField(max_length=100,null=True)
    department =models.CharField(max_length=100,null=True)
    city =models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    contact =models.CharField(max_length=100,null=True)

class EmployeeModel(models.Model):
    name =models.CharField(max_length=100,null=True)
    department =models.CharField(max_length=100,null=True)
    city =models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)

    contact =models.CharField(max_length=100,null=True)