from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    city=models.CharField(max_length=100,null=True)
    department=models.CharField(max_length=100,null=True)
    email=models.EmailField(unique=True,null=True)
    gpa=models.DecimalField(max_digits=4,decimal_places=2,null=True)
    admission_date=models.DateField(null=True)
class TeacherModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    subject=models.CharField(max_length=100,null=True)
    district=models.CharField(max_length=100,null=True)
    salary=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    joining_date=models.DateField(null=True)
    email=models.EmailField(unique=True,null=True)


class ProductModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    category=models.CharField(null=True)
    stock=models.IntegerField(null=True)
    brand=models.CharField(null=True)
    added_date=models.DateTimeField(null=True)