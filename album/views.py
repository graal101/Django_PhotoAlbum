from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'album/index.html' )

'''
def index(request):
    return HttpResponse('<h1>Привет мир!</h1>')
'''
