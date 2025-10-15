from django.shortcuts import render
from myapp.models import *
# Create your views here.

def HomePages(request):
    students=StudentsModel.objects.all()
    teacher=TeacherModel.objects.all()
    context ={
        "students": students,
        "teacher": teacher,

    }
    return render(request, "HomePages.html",context)

def StudentPages(request):
    if request.method=="POST":
        name = request.POST.get("name")
        department = request.POST.get("department")
        city = request.POST.get("city")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        StudentsModel.objects.create(
            name=name,
            deparment=department,
            city=city,
            email=email,
            contact=contact,

        )

    student=StudentsModel.objects.all()
    context={
        "student": student,
    }
    return render(request, "StudentPages.html",context)

def TeachertPages(request):
    if request.method=="POST":
        name = request.POST.get("name")
        department = request.POST.get("department")
        city = request.POST.get("city")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        TeacherModel.objects.create(
            name=name,
            deparment=department,
            city=city,
            email=email,
            contact=contact,

        )

    student=TeacherModel.objects.all()
    context={
        "student": student,
    }   

    return render(request, "TeachertPages.html",context)