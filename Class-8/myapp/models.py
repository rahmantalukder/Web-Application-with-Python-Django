from django.db import models

class StudentsModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    deparment = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    contact = models.CharField(max_length=100,null=True)
    def __str__(self):
     return self.name + " - " + self.city




class TeacherModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    deparment = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    contact = models.CharField(max_length=100,null=True)
    def __str__(self):
     return self.name + " - " + self.city + " - " +self.deparment
