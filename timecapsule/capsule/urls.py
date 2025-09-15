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
    path('create/', views.create_capsule, name='create_capsule'),
    path('capsule/view/<int:capsule_id>/', views.view_capsule, name='view_capsule'),
    path("capsule/<int:capsule_id>/mark_opened/", views.mark_opened, name='mark_opened'),
    path('capsule/<int:id>/delete/', views.delete_capsule, name='delete_capsule'),


]
