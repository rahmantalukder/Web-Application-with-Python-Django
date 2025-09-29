from django.contrib import admin
from django.urls import path
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',basePages,name='basePages'),
    path('ProductPages',ProductPages,name='ProductPages'),
    path('ProductListPages',ProductListPages,name='ProductListPages'),
    path('LoginPages',LoginPages,name='LoginPages'),

]

