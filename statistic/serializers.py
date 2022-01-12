from rest_framework import serializers
from .models import PlayerPosition, Team, Player, Tournament, Game


class PlayerPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPosition
        fields = ['id', 'name']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class PlayerSerializer(serializers.ModelSerializer):
    position_name = serializers.ReadOnlyField(source='position.name')
    team_name = serializers.ReadOnlyField(source='team.name')

    class Meta:
        model = Player
        fields = ['id', 'last_name', 'name', 'position', 'position_name', 'team', 'team_name', 'number']


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name']


class GameSerializer(serializers.ModelSerializer):
    tournament_name = serializers.ReadOnlyField(source='tournament.name')
    team_home_name = serializers.ReadOnlyField(source='team_home.name')
    team_guest_name = serializers.ReadOnlyField(source='team_guest.name')

    class Meta:
        model = Game
        fields = ['id', 'tournament', 'tournament_name', 'date_time', 'team_home', 'team_home_name', 'team_guest',
                  'team_guest_name', 'home_score', 'guest_score', 'ended']
