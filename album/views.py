from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {'title':"Фотоальбом", 'text':'Я создал этот фотоальбом, чтобы запечатлеть и сохранить самые \
                                          важные моменты моей <br> и жизни окружающих меня.\
                                          Каждая фотография в этом альбоме — это не просто изображение,\
                                          <br> а история, полная эмоций и воспоминаний.'}
    return render(request, 'album/index.html', data )

def monochrome(request):
    data = {'title': 'Ч/Б архив'}
    return render(request, 'album/monochrome.html', data )

'''
def index(request):
    return HttpResponse('<h1>Привет мир!</h1>')
'''
