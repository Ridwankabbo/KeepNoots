from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singup/', views.singUp, name='singup'),
    path('register-usr', views.register_user, name='register-usr'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('write-noots', views.write_noots, name='write-noots'),
    path('add-noots', views.add_or_upgrade_noots, name="add-noots" ),
    path('noots-page', views.noots_page, name='noots-page'),
    path('delete-noot/<int:noot_id>/', views.deleteNoot, name='delete.noot'),
    path('edite-noot/<int:noot_id>/', views.editeNoot, name='edite.noot')
]
