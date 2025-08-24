from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('game', views.play, name='play'),
    path('game/move', views.move, name='move')
] 