
from django.contrib import admin
from django.urls import path
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',DashboardPages,name="DashboardPages"),    
    path('StudentPages',StudentPages,name="StudentPages"),
    path('TeacherPages',TeacherPages,name="TeacherPages"),
    path('emlpoyeePages',emlpoyeePages,name="emlpoyeePages"),
]
