from django.shortcuts import render
from myapp.models import *
# Create your views here.
def DashboardPages(request):
    department=StudentModel.objects.values_list("department",flat=True).distinct()

    selected_department=request.GET.get("department")

    if selected_department:
        students=StudentModel.objects.filter(department=selected_department)
    else:
        students=StudentModel.objects.all()
    context={
        'students':students,
        'department':department,
        'selected_department':selected_department,
    }
    return render (request, "Dashbaord.html",context)

def StudentPages(request):

    departments=StudentModel.objects.values_list("department",flat=True).distinct()
    setect_department=request.GET.get("department")

    if setect_department:
        student=StudentModel.objects.filter(department=setect_department)
    else:
        student=StudentModel.objects.all()
    context={
        'student':student,
        'departments':departments,
        'setect_department':setect_department,
    }
    return render (request, "StudentPages.html",context)

def TeacherPages(request):

    subject1=TeacherModel.objects.filter("subject").distinct()
    select_subject=request.GET.get("")
    if select_subject:
        subject2=TeacherModel.objects.all(subject=select_subject)
    else:
        subject=TeacherModel.objects.all()
    context={
        "subject":subject1,
        "subject":subject2,
        "select_subject":select_subject,

    }

    return render (request, "TeacherPages.html",context)
def ProductPages(request):
    data=ProductModel.objects.all()
    context={
        "product":data
    }
    return render (request, "ProductPages.html",context)