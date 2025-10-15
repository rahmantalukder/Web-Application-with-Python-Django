from django.contrib import admin
from django.urls import path
from relationship.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePages, name='homePages'),
    path('employeePages', employeePages, name='employeePages'),
    path('personalPages', personalPages, name='personalPages'),
]
