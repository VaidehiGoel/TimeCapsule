from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, 'capsule/home.html', {
        'page': 'home',
        'timestamp': datetime.now().timestamp()
    })
# Create your views here.

def future(request):
    return render(request, 'capsule/future.html', {'page': 'future'})

def opened(request):
    return render(request, 'capsule/opened.html', {'page': 'opened'})
