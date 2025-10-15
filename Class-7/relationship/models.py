from django.db import models

# Create your models here.
class Designation(models.Model):
    dept_name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.dept_name

class EmployeeModel(models.Model):
    DESIGNATON_TYPES =[
        ('manage', 'Manage' ),
        ('ceo', 'CEO' ),
        ('admin', 'Admin' ),
        ('staff', 'Staff' ),
    ]
    name = models.CharField(max_length=100, null=True)
    dept = models.ForeignKey(Designation,on_delete=models.SET_NULL, related_name='employee_dept', null=True)
    designation = models.CharField(choices=DESIGNATON_TYPES,max_length=100, null=True)
    salary = models.PositiveIntegerField( null=True)
    def __str__(self):
        return self.name


class PersonalModel(models.Model):
    employee = models.OneToOneField(EmployeeModel, on_delete=models.CASCADE, related_name='employee_name', null=True)
    email = models.EmailField( null=True)
    address = models.TextField( null=True)
    mobile = models.CharField(max_length=12, null=True)
    def __str__(self):
        return self.employee.name 
