from django.urls import path
from . import views


    
urlpatterns = [
    path('', views.home, name='home'),
    path('future/', views.future, name='future'),
    path('opened/', views.opened, name='opened'),

]
