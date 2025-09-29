from django.shortcuts import render
from myapp.models import *

def DashboardPages(request):
    data=S
    return render(request, "DashboardPages.html")

def StudentPages(request):
    if request.method == "POST":
        student_name = request.POST.get("name")
        Department_name = request.POST.get("Department")
        roll_name = request.POST.get("roll")
        Admission_Data = request.POST.get("Admission")

        student=StudentModel(
            name=student_name,
            department=Department_name,
            roll=roll_name,
            Admission=Admission_Data,
        ).save()

    # ✅ POST হোক বা GET হোক, সবসময় নিচের অংশ চলবে
    department = StudentModel.objects.values_list("department", flat=True).distinct()
    selected_department = request.GET.get("department")

    if selected_department:
        student = StudentModel.objects.filter(department=selected_department)
    else:
        student = StudentModel.objects.all()

    context = {
        'student': student,
        'department': department,
        'selected_department': selected_department,
    }
    return render(request, "StudentPages.html", context)

def TeacherPages(request):
    return render(request, "TeacherPages.html")

def emlpoyeePages(request):
    return render(request, "emlpoyeePages.html")
