from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('player_position', views.player_position_list),
    path('players', views.players_list),
    path('players/<int:pk>', views.players_detail),
    path('teams', views.team_list),
    path('teams/<int:pk>', views.team_detail),
    path('tournaments', views.tournament_list),
    path('tournaments/<int:pk>', views.tournament_detail),
    path('games', views.game_list),
    path('games/<int:pk>', views.game_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
