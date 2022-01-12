from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Team, PlayerPosition, Player, Tournament, Game
from . import serializers


@api_view(['GET'])
def player_position_list(request):
    queryset = PlayerPosition.objects.all().order_by('id')
    player_position_serializer = serializers.PlayerPositionSerializer(queryset, many=True)
    return JsonResponse(player_position_serializer.data, safe=False)


@api_view(['GET', 'POST'])
def team_list(request):

    if request.method == 'GET':
        queryset = Team.objects.all().order_by('name')
        team_serializer = serializers.TeamSerializer(queryset, many=True)
        return JsonResponse(team_serializer.data, safe=False)

    elif request.method == 'POST':
        team_data = JSONParser().parse(request)
        team_serializer = serializers.TeamSerializer(data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return JsonResponse({'message': 'The team does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        team_data = JSONParser().parse(request)
        team_serializer = serializers.TeamSerializer(team, data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return JsonResponse({'message': 'Team was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def players_list(request):

    if request.method == 'GET':
        queryset = Player.objects.all().order_by('last_name')
        player_serializer = serializers.PlayerSerializer(queryset, many=True)
        return JsonResponse(player_serializer.data, safe=False)

    elif request.method == 'POST':
        player_data = JSONParser().parse(request)
        player_serializer = serializers.PlayerSerializer(data=player_data)
        if player_serializer.is_valid():
            player_serializer.save()
            return JsonResponse(player_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(player_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def players_detail(request, pk):

    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return JsonResponse({'message': 'The player does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        player_serializer = serializers.PlayerSerializer(player)
        return JsonResponse(player_serializer.data, safe=False)

    elif request.method == 'PUT':
        player_data = JSONParser().parse(request)
        player_serializer = serializers.PlayerSerializer(player, data=player_data)
        if player_serializer.is_valid():
            player_serializer.save()
            return JsonResponse(player_serializer.data)
        return JsonResponse(player_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player.delete()
        return JsonResponse({'message': 'Player was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def tournament_list(request):

    if request.method == 'GET':
        queryset = Tournament.objects.all().order_by('id')
        tournament_serializer = serializers.TournamentSerializer(queryset, many=True)
        return JsonResponse(tournament_serializer.data, safe=False)

    elif request.method == 'POST':
        tournament_data = JSONParser().parse(request)
        tournament_serializer = serializers.TournamentSerializer(data=tournament_data)
        if tournament_serializer.is_valid():
            tournament_serializer.save()
            return JsonResponse(tournament_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tournament_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def tournament_detail(request, pk):
    try:
        tournament = Tournament.objects.get(pk=pk)
    except Tournament.DoesNotExist:
        return JsonResponse({'message': 'The tournament does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        tournament_data = JSONParser().parse(request)
        tournament_serializer = serializers.TeamSerializer(tournament, data=tournament_data)
        if tournament_serializer.is_valid():
            tournament_serializer.save()
            return JsonResponse(tournament_serializer.data)
        return JsonResponse(tournament_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tournament.delete()
        return JsonResponse({'message': 'Tournament was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def game_list(request):

    if request.method == 'GET':
        queryset = Game.objects.all().order_by('id')
        game_serializer = serializers.GameSerializer(queryset, many=True)
        return JsonResponse(game_serializer.data, safe=False)

    elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = serializers.GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serializer = serializers.GameSerializer(game)
        return JsonResponse(game_serializer.data, safe=False)

    elif request.method == 'PUT':
        game_data = JSONParser().parse(request)
        game_serializer = serializers.GameSerializer(game, data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data)
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        game.delete()
        return JsonResponse({'message': 'Game was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
