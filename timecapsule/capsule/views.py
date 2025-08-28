from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home')
def future(response):
    return HttpResponse('future')
def opened(response):
    return HttpResponse('opened')
