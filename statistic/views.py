# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Division, PlayerPosition, TournamentType, EventType, Team
from . import serializers


@api_view(['GET'])
def division_list(request):
    queryset = Division.objects.all().order_by('id')
    division_serializer = serializers.DivisionSerializer(queryset, many=True)
    return JsonResponse(division_serializer.data, safe=False)


@api_view(['GET'])
def player_position_list(request):
    queryset = PlayerPosition.objects.all().order_by('id')
    player_position_serializer = serializers.PlayerPositionSerializer(queryset, many=True)
    return JsonResponse(player_position_serializer.data, safe=False)


@api_view(['GET'])
def tournament_type_list(request):
    queryset = TournamentType.objects.all().order_by('id')
    tournament_type_serializer = serializers.TournamentTypeSerializer(queryset, many=True)
    return JsonResponse(tournament_type_serializer.data, safe=False)


@api_view(['GET'])
def event_type_list(request):
    queryset = EventType.objects.all().order_by('id')
    event_type_serializer = serializers.EventTypeSerializer(queryset, many=True)
    return JsonResponse(event_type_serializer.data, safe=False)


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


@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return JsonResponse({'message': 'The team does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        team_serializer = serializers.TeamSerializer(team)
        return JsonResponse(team_serializer.data, safe=False)

    elif request.method == 'PUT':
        team_data = JSONParser().parse(request)
        team_serializer = serializers.TeamSerializer(team, data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return JsonResponse({'message': 'Team was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)