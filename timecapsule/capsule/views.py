from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
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

@login_required
def create_capsule(request):
    if request.method=="POST":
        form=CapsuleForm(request.POST,request.FILES)
        if form.is_valid():
            capsule=form.save(commit=False)
            capsule.user=request.user
            capsule.save()
            return redirect('/')
    else:
        form=CapsuleForm()
    return render(request, 'capsule/create_capsule.html', {'form': form})

@login_required
def opened(request):
    opened = Capsule.objects.filter(user=request.user, unlock_date__lte=now())
    return render(request, 'capsule/opened.html', {'opened': opened,'page': 'opened'})


@login_required
def future(request):
    unopened = Capsule.objects.filter(user=request.user, unlock_date__gt=now())
    return render(request, 'capsule/future.html', {'unopened': unopened ,'page': 'future'})


from datetime import datetime


def home(request):

    return render(request, 'capsule/home.html', {
        'page': 'home',
        'timestamp': datetime.now().timestamp()
    })
# Create your views here.



