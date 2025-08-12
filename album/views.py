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
    
def dacha(request):
    lst = ['https://na-dache.pro/uploads/posts/2021-04/1619788199_14-p-na-uchastke-leto-na-dache-14.jpg',
           'https://pro-dachnikov.com/uploads/posts/2021-07/1627055128_30-p-dachnie-uchastki-obichnoi-dachi-30.jpg',
            'https://design-homes.ru/images/galery/2376/besedka-dlya-dachi_5f43be4b472f0.jpg',]
            
    data = {'title': 'Фото дача', 'photo':lst}
    return render(request, 'album/album.html', data )
    
def cat(request):
    lst = ['https://c.wallhere.com/photos/ba/b3/1920x1270_px_blue_cat_eyes_pose-1912453.jpg',
           'https://pichold.ru/wp-content/uploads/2018/10/7ea9f65adc25bc7b0c65838809966e84.jpg',
            'https://i.ytimg.com/vi/7LPC2_A7S4s/maxresdefault.jpg',
            'https://www.1zoom.ru/big2/613/322342-alexfas01.jpg',]
            
    data = {'title': 'Фото кота', 'photo':lst}        
    return render(request, 'album/album.html', data )

'''
def index(request):
    return HttpResponse('<h1>Привет мир!</h1>')
'''
