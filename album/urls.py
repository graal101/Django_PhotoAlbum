# Файл создан из основного urls.py
from django.conf import settings  # Добавлено при подк. загрузки картинок
from django.conf.urls.static import static  # Добавлено при подк. загрузки картинок

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monochrome/', views.monochrome, name='monochrome'),
    path('dacha/', views.dacha, name='dacha'),
    path('kat/', views.kat, name='kat'),
    path('trip/', views.trip, name='trip'),
    path('upload_img/', views.upload_img, name='upload_img')
    
]

if settings.DEBUG:  # Добавлено при подк. загрузки картинок
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
