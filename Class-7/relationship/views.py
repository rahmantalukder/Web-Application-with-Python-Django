from django.shortcuts import render,redirect
from relationship.models import *
# Create your views here.
def homePages(request):
    if request.method=="POST":
        email= request.POST.get("email")
        address= request.POST.get("address")
        mobile= request.POST.get("mobile")
        department= request.POST.get("department")
        dept_data=EmployeeModel.objects.get(id=department)

        PersonalModel.objects.create(
            employee=dept_data,
            email=email,
            address=address,
            mobile=mobile,
        )
    deparment=Designation.objects.all()
    personal=PersonalModel.objects.all()
    context= {
        "deparment": deparment,
        "personal" :personal,
    }

    return render(request, 'homePages.html',context)

def employeePages(request):
    if request.method=="POST":
        name= request.POST.get("name")
        designation= request.POST.get("designation")
        salary= request.POST.get("salary")
        employee= request.POST.get("employee")
        dept_data=Designation.objects.get(id=employee)

        EmployeeModel.objects.create(
            name=name,
            employee=dept_data,
            salary=salary,
            designation=designation,
           
        )
        return redirect ("personalPages")
    deparment=Designation.objects.all()


    context= {
        "deparment": deparment,

    }
    return render(request, 'employeePages.html',context)

def personalPages(request):
    employee=PersonalModel.objects.all()
    context= {
    "employee":employee,
    }
    return render(request, 'personalPages.html',context)