from django.shortcuts import render

# Create your views here.
def DepartmentPage(requiset):

    return render(requiset, "DepartmentPages.html")

def EmployeePage(requiset):
    
    return render(requiset, "EmployeePage.html")

def BasicInfoPage(requiset):
    
    return render(requiset, "BasicInfoPage.html")