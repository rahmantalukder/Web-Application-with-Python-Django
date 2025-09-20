from django.shortcuts import render
from myapp.models import *
def DashboardPages(request):
    student=StudentModel.objects.all()
    context={
        'student':student
    }
    return render(request, "DashboardPages.html",context)

def StudentPages(request):
    if request.method=="POST":
        student_name=request.POST.get('name')
        department_name=request.POST.get('department')
        city_name=request.POST.get('city')
        email_name=request.POST.get('email')
        contact_name=request.POST.get('contact')
        student=StudentModel(
            name=student_name,
            department=department_name,
            city=city_name,
            email=email_name,
            contact=contact_name,
        )
        student.save()
     
    student=StudentModel.objects.all()
    context={
        'student':student
    }
    return render (request,"StudentPages.html",context)


def TeacherPages(request):
    
    return render (request,"TeacherPages.html")

def EmployeePages(request):
    
    return render (request,"employeePages.html")