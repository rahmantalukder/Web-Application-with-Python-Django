from django.shortcuts import render
from myapp.models import *

def HomePages(request):
    # Handle form submission (POST)
    if request.method == "POST":
        student_name   = request.POST.get("name")
        roll_name      = request.POST.get("roll")
        department_name= request.POST.get("department")

        StudentModel.objects.create(
            name=student_name,
            roll=roll_name,
            department=department_name,
        )


    student  = StudentModel.objects.all()
    course   = CourseModel.objects.all()
    teacher  = TeacherModel.objects.all()
    students = StudentModel.objects.all().order_by("roll")

    context  = {
        "student": student,
        "course": course,
        "teacher": teacher,
        "students": students,
    }
    return render(request, "HomePages.html", context)


def StudentPages(request):
    return render(request, "StudentPages.html")

def CoursePages(request):
    return render(request, "CoursePages.html")

def TeacherPages(request):
    return render(request, "TeacherPages.html")
