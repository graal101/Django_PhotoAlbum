import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import UplPictForm

import requests  # Доустанавливается

from .models import Visitors
from .models import UplPict

    
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
    return render(request, 'album/album.html', sample('Фото дачи.', 'fathenda'))


def kat(request):
    """Страница о коте."""
    return render(request, 'album/album.html', sample('Фото кота.', 'cat'))


def trip(request):
    """Страница о поездках."""
    return render(request, 'album/album.html', sample('Фото поездок', 'trip'))
    
    
def feedback(request):
    """Обратная связь с админом."""
    return render(request, 'album/feedback.html', {'title':'Связаться с админом.'})
  # =============================================Functions=======================================================
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

def sample(h1: str, smp: str) -> dict:
    """Функция для выборки из модели картинок.
       :smp: слово для фильтрации в бд.
       :h1: заголовок посылаемый в заголовок страницы. 
    """
    instances = UplPict.objects.filter(name=smp)
    lst = [instance.UpPict_Img.name for instance in instances if instance.UpPict_Img]
    return {'title': h1, 'photo': lst, 'MEDIA_URL': settings.MEDIA_URL}
    
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

  # ==========================================================================================================
