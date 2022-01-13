import json

from django.test import TestCase, Client
from rest_framework import status

from .models import Team
from django.urls import reverse
from .serializers import TeamSerializer

client = Client()


# class TeamModelTest(TestCase):
#     def setUp(self):
#         Team.objects.create(
#             name='Волга')
#         Team.objects.create(
#             name='Витязь')
#         Team.objects.create(
#             name='Авангард')
#         Team.objects.create(
#             name='Патриот')
#
#     def test_team_content(self):
#         team = Team.objects.get(id=1)
#         expected_team_name = f'{team.name}'
#         self.assertEquals(expected_team_name, 'Волга')
#
#
# class GetAllTeamsTest(TestCase):
#
#     def test_get_teams(self):
#         response = client.get('/api/teams')
#         teams = Team.objects.all()
#         serializer = TeamSerializer(teams, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class CreateNewTeamTest(TestCase):
#     def setUp(self):
#         self.valid_payload = {
#             'name': 'Сталь Каскад'
#         }
#         self.invalid_payload = {
#             'name': '',
#         }
#
#     def test_create_valid_team(self):
#         response = client.post('/api/teams',
#                                data=json.dumps(self.valid_payload),
#                                content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_create_invalid_puppy(self):
#         response = client.post('/api/teams',
#                                data=json.dumps(self.invalid_payload),
#                                content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class UpdateSingleTeamTest(TestCase):
#     def setUp(self):
#         self.volga = Team.objects.create(name='Волга')
#         self.vityaz = Team.objects.create(name='Витязь')
#         self.valid_payload = {
#             'name': 'Волга 2'
#         }
#         self.invalid_payload = {
#             'name': ''
#         }
#
#     def test_valid_update_team(self):
#         response = client.put('/api/teams/' + str(self.volga.pk),
#                               data=json.dumps(self.valid_payload),
#                               content_type='application/json'
#                               )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_invalid_update_team(self):
#         response = client.put('/api/teams/' + str(self.vityaz.pk),
#                               data=json.dumps(self.invalid_payload),
#                               content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleTeamTest(TestCase):
    def setUp(self):
        self.volga = Team.objects.create(name='Волга')
        self.vityaz = Team.objects.create(name='Витязь')

    def test_valid_delete_team(self):
        response = client.delete('/api/teams/' + str(self.vityaz.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_team(self):
        response = client.delete('/api/teams/' + str(30))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
