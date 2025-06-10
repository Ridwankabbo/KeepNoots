from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singup/', views.singUp, name='singup'),
    path('login/', views.login, name='login')
]
