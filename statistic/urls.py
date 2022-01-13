from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import team_list, team_detail, player_position_list, players_list, players_detail, tournament_detail, \
    tournament_list, game_list, game_detail

urlpatterns = [
    path('player_position', player_position_list),
    path('players', players_list),
    path('players/<int:pk>', players_detail),
    path('teams', team_list),
    path('teams/<int:pk>', team_detail),
    path('tournaments', tournament_list),
    path('tournaments/<int:pk>', tournament_detail),
    path('games', game_list),
    path('games/<int:pk>', game_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
