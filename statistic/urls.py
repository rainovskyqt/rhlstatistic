from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('divisions', views.division_list),
    path('player_position', views.player_position_list),
    path('tournament_type', views.tournament_type_list),
    path('event_type', views.event_type_list),
    path('teams', views.team_list),
    path('teams/<int:pk>', views.team_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
