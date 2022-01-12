from django.db import models


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlayerPosition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlayerTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    number = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class TournamentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(TournamentType, on_delete=models.CASCADE)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date_time = models.DateTimeField
    team_home = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_guest = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GameResults(models.Model):
    home_score = models.IntegerField(max_length=3)
    guest_score = models.IntegerField(max_length=3)
    shots_on_goal = models.IntegerField(max_length=3)
    blocked_shots = models.IntegerField(max_length=3)

    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GameEvent(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    time = models.IntegerField(max_length=3)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.name