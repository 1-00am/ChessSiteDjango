from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('game/new', views.new_game, name='new_game'),
    path('game/load', views.load_game, name='load_game'),
    path('game/<int:id>', views.game, name='game'),
    path('game/<int:id>/move', views.move, name='move')
] 