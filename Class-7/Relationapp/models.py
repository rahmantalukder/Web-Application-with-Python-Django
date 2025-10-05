from django.db import models

# Create your models here.
class  DepartmentModel(models.Model):
    department_name =models.CharField(max_length=100,null=True )

class EmployeeModel(models.Model):
    employee_name  = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    employee_idno= models.CharField(max_length=100,null=True)
    department  = models.ForeignKey(DepartmentModel, on_delete=models.SET_NULL,related_name='employee_dept',null=True)
    disignation = models.CharField(max_length=100, null=True)
    salary = models.CharField(max_length=100, null=True)
class BasicInfoModel(models.Model):
    employee = models.OneToOneField(EmployeeModel, on_delete=models.CASCADE,related_name='employree_info')
    gender   = models.CharField(max_length=100, null=True)
    another_rel = models.OneToOneField(EmployeeModel,on_delete=models.CASCADE,null=True)
    email = models.EmailField(unique=True, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)