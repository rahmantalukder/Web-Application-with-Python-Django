from django.contrib import admin
from django.urls import path, include  # ✅ from django.urls
from myapp import views  # if you need direct view imports

urlpatterns = [
    path('', include('myapp.urls')),  # ✅ Correct include usage
]
