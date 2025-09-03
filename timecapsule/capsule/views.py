from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'capsule/home.html')
def future(request):
    return render(request, 'capsule/future.html')
def opened(request):
    return render(request, 'capsule/opened.html')
