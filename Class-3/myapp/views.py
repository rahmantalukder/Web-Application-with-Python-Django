from django.shortcuts import render
from myapp.models import *
# Create your views here.
def StudentPages(request):

    if request.method=="POST":
        student_name=request.POST.get("name")
        department_name=request.POST.get("department")
        age_name=request.POST.get("age")
        email_name=request.POST.get("email")
        contact_name=request.POST.get("contact")
        student=StudentModel(
            name=student_name,
            department=department_name,
            age=age_name,
            email=email_name,
            contact=contact_name,
        )
        student.save()


    data=StudentModel.objects.all()
    departments=StudentModel.objects.values_list("department",flat=True).distinct()
    context={
        'student':data,
        'departments':departments,
        }

    return render(request, "studentPagas.html", context)