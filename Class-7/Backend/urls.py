
from django.contrib import admin
from django.urls import path
from Relationapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DepartmentPage, name='DepartmentPage'),
    path('EmployeePage', EmployeePage, name='EmployeePage'),
    path('BasicInfoPage', BasicInfoPage, name='BasicInfoPage'),
]
