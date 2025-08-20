import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import UplPictForm

import requests  # Доустанавливается

from .models import Visitors
from .models import UplPict


def load_image_paths(directory):
    """Загрузка путь изображений."""
    image_paths = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG')):
            image_paths.append(os.path.join(directory, filename))
    return image_paths

def referer(request):
    """Получения реферера."""
    referer = request.META.get('HTTP_REFERER')
    
    if referer:
        return referer
    else:
        return 'Неопределен'

def get_client_ip(request):
    """Получение юзер-агента посетителя."""
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # Получаем первый IP из списка
    else:
        ip = request.META.get('REMOTE_ADDR')  # Если заголовок отсутствует, используем REMOTE_ADDR
    return ip


def index(request):
    """Главная страница."""
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT')
    ref = referer(request)
    visit = Visitors(ip=ip, user_agent=user_agent, ref = ref)
    visit.save()
    data = {'title': 'Фотоальбом', 'text': 'Я создал этот фотоальбом, чтобы запечатлеть и сохранить самые \
                                          важные моменты моей <br> и жизни окружающих меня.\
                                          Каждая фотография в этом альбоме — это не просто изображение,\
                                          <br> а история, полная эмоций и воспоминаний.'}
    return render(request, 'album/index.html', data)


def monochrome(request):
    """Страница чб архива."""
    lst = []
    data = {'title': 'Ч/Б архив', 'photo': lst}
    return render(request, 'album/monochrome.html', data)


def dacha(request):
    """Страница о даче."""
    trip_dir = os.path.join(settings.BASE_DIR, 'album', 'static', 'album', 'img', 'base', 'fathenda')
    if not os.path.exists(trip_dir):
        return render(request, 'album/album.html', {'title': f'Ошибка директории - {trip_dir}',
                      'photos': [], 'error': 'Директория не найдена.'})
    lst1 = [f for f in os.listdir(trip_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG'))]
    data = {'title': 'Фото дачи', 'photo': lst1, 'num': 1}
    return render(request, 'album/album.html', data)


def kat(request):
    """Страница о коте."""
    trip_dir = os.path.join(settings.BASE_DIR, 'album', 'static', 'album', 'img', 'base', 'cat')
    if not os.path.exists(trip_dir):
        return render(request, 'album/album.html', {'title': f'Ошибка директории - {trip_dir}',
                      'photos': [], 'error': 'Директория не найдена.'})
    lst1 = [f for f in os.listdir(trip_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG'))]
    data = {'title': 'Фото кота', 'photo': lst1, 'num': 2}
    return render(request, 'album/album.html', data)


def trip(request):
    """Страница о поездках."""
    trip_dir = os.path.join(settings.BASE_DIR, 'album', 'static', 'album', 'img', 'base', 'trip')
    if not os.path.exists(trip_dir):
        return render(request, 'album/album.html', {'title': f'Ошибка директории - {trip_dir}',
                      'photos': [], 'error': 'Директория не найдена.'})
    lst = [f for f in os.listdir(trip_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG'))]
    data = {'title': 'Фото поездок', 'photo': lst, 'num': 3}
    return render(request, 'album/album.html', data)


def upload_img(request):
    """Загрузка файла на сервер."""
    if request.method == 'POST':
        form = UplPictForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return HttpResponse('<h1>Успешно загружено!..</h1>')
    else:
        form = UplPictForm()
    return render(request, 'album/load_jpg.html', {'form': form})
