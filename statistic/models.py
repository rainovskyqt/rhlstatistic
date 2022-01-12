from django.db import models


# Create your models here.
from django.utils.formats import date_format


class Team(models.Model):
    name = models.CharField(max_length=100)

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
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.CharField(max_length=2)

    def __str__(self):
        return self.last_name + ' ' + self.name


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    team_home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home')
    team_guest = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='guest')
    home_score = models.IntegerField(default=0)
    guest_score = models.IntegerField(default=0)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return date_format(self.date_time) + ' ' + self.tournament.name + ' ' + self.team_home.name + ' - ' + \
               self.team_guest.name  \

