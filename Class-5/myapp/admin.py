from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(StudentModel)
admin.site.register(CourseModel)
admin.site.register(TeacherModel)