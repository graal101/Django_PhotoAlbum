import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import Visitors
import requests # Доустанавливается

def load_image_paths(directory):
    """Загрузка путь изображений."""
    image_paths = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG')):  # Укажите нужные форматы изображений
            image_paths.append(os.path.join(directory, filename))
    return image_paths
    
def get_client_ip(request):
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # Получаем первый IP из списка
    else:
        ip = request.META.get('REMOTE_ADDR')  # Если заголовок отсутствует, используем REMOTE_ADDR
    return ip

    
# Create your views here.
def index(request):
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT')
    visit = Visitors(ip=ip, user_agent=user_agent)
    visit.save()
    data = {'title':"Фотоальбом", 'text':'Я создал этот фотоальбом, чтобы запечатлеть и сохранить самые \
                                          важные моменты моей <br> и жизни окружающих меня.\
                                          Каждая фотография в этом альбоме — это не просто изображение,\
                                          <br> а история, полная эмоций и воспоминаний.'}
    return render(request, 'album/index.html', data )

def monochrome(request):
    lst = []
    data = {'title': 'Ч/Б архив', 'photo':lst}
    return render(request, 'album/monochrome.html', data )
    
def dacha(request):
    trip_dir = os.path.join(settings.BASE_DIR, 'album','static', 'album', 'img', 'base', 'fathenda')
    # Проверяем, существует ли директория
    if not os.path.exists(trip_dir):
        return render(request, 'album/album.html', {'title': f'Ошибка директории - {trip_dir}',
         'photos': [], 'error': 'Директория не найдена.'})
    lst1 = [f for f in os.listdir(trip_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG'))]
    data = {'title': 'Фото кота', 'photo':lst1, 'num':1}  
    return render(request, 'album/album.html', data )
    
def kat(request):
    trip_dir = os.path.join(settings.BASE_DIR, 'album','static', 'album', 'img', 'base', 'cat')
    # Проверяем, существует ли директория
    if not os.path.exists(trip_dir):
        return render(request, 'album/album.html', {'title': f'Ошибка директории - {trip_dir}',
         'photos': [], 'error': 'Директория не найдена.'})
    lst1 = [f for f in os.listdir(trip_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG'))]
    data = {'title': 'Фото кота', 'photo':lst1, 'num':2}        
    return render(request, 'album/album.html', data)
    
def trip(request):
    trip_dir = os.path.join(settings.BASE_DIR, 'album','static', 'album', 'img', 'base', 'trip')
    # Проверяем, существует ли директория
    if not os.path.exists(trip_dir):
        return render(request, 'album/album.html', {'title': f'Ошибка директории - {trip_dir}',
         'photos': [], 'error': 'Директория не найдена.'})
    lst = [f for f in os.listdir(trip_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG'))]
    data = {'title': 'Фото поездок', 'photo':lst, 'num':3}        
    return render(request, 'album/album.html', data )

'''
def index(request):
    return HttpResponse('<h1>Привет мир!</h1>')
'''
