from django.urls import path
from django.contrib import admin
from . import views


    
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('future/', views.future, name='future'),
    path('opened/', views.opened, name='opened'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
