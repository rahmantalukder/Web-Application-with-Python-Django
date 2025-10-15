
from django.contrib import admin
from django.urls import path
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePages, name='HomePages'),
    path('StudentPages',StudentPages, name='StudentPages'),
    path('TeachertPages',TeachertPages, name='TeachertPages'),

]
