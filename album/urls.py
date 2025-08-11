# Файл создан из основного urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monochrome/', views.monochrome, name='monochrome'),
]
