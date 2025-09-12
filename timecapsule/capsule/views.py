from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Account created successfully! Please login.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match!")
    return render(request, 'capsule/registration.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'capsule/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'capsule/home.html')
def future(response):
    return HttpResponse('future')
def opened(response):
    return HttpResponse('opened')
