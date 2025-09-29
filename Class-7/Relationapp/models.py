from django.db import models

# Create your models here.
class  DepModel(models.Model):
    dept_name=models.CharField(max_length=100,null=True )

class EmployeeModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    dept = models.ForeignKey(DepModel, on_delete=models.SET_NULL,related_name='employee_dept',null=True)

class ParsonalInfoModel(models.Model):
    employee = models.OneToOneField(EmployeeModel, on_delete=models.CASCADE,related_name='employree_info')
    another_rel = models.OneToOneField(EmployeeModel,on_delete=models.CASCADE,null=True)


