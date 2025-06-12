from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singup/', views.register_user, name='singup'),
    # path('register-usr', views.register_user, name='register-usr'),
    path('login/', views.login, name='login'),
    # path('login-usr', )
    path('write-noots', views.write_noots, name='write-noots'),
    path('add-noots', views.add_noots, name="add-noots" ),
    path('noots-page', views.noots_page, name='noots-page')
]
