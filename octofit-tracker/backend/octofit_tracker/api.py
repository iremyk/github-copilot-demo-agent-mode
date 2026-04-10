from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardEntryViewSet, basename='leaderboardentry')

urlpatterns = [
    path('', views.api_root, name='api-root'),
]

urlpatterns += router.urlsfrom rest_framework import routers, serializers, viewsets
from django.urls import path, include
from djongo import models
from pymongo import MongoClient
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Serializers
class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    team = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField()

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField()
    team = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    team = serializers.CharField()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

# API Views
@api_view(['GET'])
def users_list(request):
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db = client['octofit_db']
    users = list(db.users.find({}, {'_id': 0}))
    return Response(users)

@api_view(['GET'])
def teams_list(request):
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db = client['octofit_db']
    teams = list(db.teams.find({}, {'_id': 0}))
    return Response(teams)

@api_view(['GET'])
def activities_list(request):
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db = client['octofit_db']
    activities = list(db.activities.find({}, {'_id': 0}))
    return Response(activities)

@api_view(['GET'])
def leaderboard_list(request):
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db = client['octofit_db']
    leaderboard = list(db.leaderboard.find({}, {'_id': 0}))
    return Response(leaderboard)

@api_view(['GET'])
def workouts_list(request):
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db = client['octofit_db']
    workouts = list(db.workouts.find({}, {'_id': 0}))
    return Response(workouts)

urlpatterns = [
    path('api/users/', users_list),
    path('api/teams/', teams_list),
    path('api/activities/', activities_list),
    path('api/leaderboard/', leaderboard_list),
    path('api/workouts/', workouts_list),
]
