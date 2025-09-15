from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.timezone import now
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime


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
        form=CapsuleForm(request.POST,request.FILES,request=request)
        if form.is_valid():
            capsule=form.save(commit=False)
            capsule.user=request.user
            capsule.save()
            if capsule.unlock_date > now():
                return redirect('future')
            else:
                capsule.is_opened = True
                capsule.save()
                return redirect('opened')
    else:
        form=CapsuleForm(request=request)
    return render(request, 'capsule/create_capsule.html', {'form': form})

@login_required
def opened(request):
    opened_capsules = Capsule.objects.filter(user=request.user, is_opened=True)
    return render(request, 'capsule/opened.html', {'opened': opened_capsules, 'page': 'opened'})

@login_required
def toggle_view(request, capsule_id):
    """Toggle visibility of message/media in Opened capsules"""
    capsule = get_object_or_404(Capsule, id=capsule_id, user=request.user)
    capsule.viewed_once = not capsule.viewed_once
    capsule.save()
    return redirect('opened')

@login_required
def future(request):
    unopened = Capsule.objects.filter(
        user=request.user,
        unlock_date__gt=now(),
        is_opened=False
    )
    return render(request, 'capsule/future.html', {'unopened': unopened, 'page': 'future'})



@login_required
def view_capsule(request, capsule_id):
    """When user clicks 'View Now' in Future page"""
    capsule = get_object_or_404(Capsule, id=capsule_id, user=request.user)

    # Debug prints
    print("DEBUG: capsule.unlock_date =", capsule.unlock_date)
    print("DEBUG: now =", now())

    if capsule.unlock_date <= now():
        return render(request, 'capsule/view_capsule.html', {'capsule': capsule})
    else:
        messages.error(request, "You cannot open this capsule yet!")
        return redirect('future')

    
    
@login_required
def mark_opened(request, capsule_id):
    capsule = get_object_or_404(Capsule, id=capsule_id)
    if request.method == "POST":
        capsule.is_opened=True
        capsule.save()
        return redirect("opened")   # ✅ redirect straight to opened page
    return redirect("future")


@login_required
def delete_capsule(request, id):
    capsule = get_object_or_404(Capsule, id=id)
    capsule.delete()
    messages.success(request, "Capsule deleted successfully!")
    # Redirect to the page user came from
    return redirect(request.META.get('HTTP_REFERER', '/'))

def home(request):

    return render(request, 'capsule/home.html', {
        'page': 'home',
        'timestamp': datetime.now().timestamp()
    })
# Create your views here.



