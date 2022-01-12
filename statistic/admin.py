from django.contrib import admin
from .models import Division, Team, PlayerPosition, Player, PlayerTeam, TournamentType, Tournament, Game, GameResult,\
   EventType, GameEvent
# Register your models here.
admin.site.register(Division)
admin.site.register(Team)
admin.site.register(PlayerPosition)
admin.site.register(Player)
admin.site.register(PlayerTeam)
admin.site.register(TournamentType)
admin.site.register(Tournament)
admin.site.register(Game)
admin.site.register(GameResult)
admin.site.register(EventType)
admin.site.register(GameEvent)
