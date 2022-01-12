from django.contrib import admin
from .models import  Team, PlayerPosition, Player, Tournament, Game

# Register your models here.
admin.site.register(Team)
admin.site.register(PlayerPosition)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(Game)
