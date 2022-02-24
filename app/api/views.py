from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters


# def index(request):
#     return HttpResponse("Hola migueluki")


class MovieViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MovieCategoriesViewSet(viewsets.ModelViewSet):
    queryset = MovieCategories.objects.all()
    serializer_class = MovieCategoriesSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ActorViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'genre']
    queryset = Actor.objects.all()
    serializer_class = MovieCategoriesSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MoviesActorsViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'genre']
    queryset = MovieActor.objects.all()
    serializer_class = MovieActorSerializer
    # permission_classes = [permissions.IsAuthenticated]

class DirectorViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    queryset = Director.objects.all()
    serializer_class = MovieCategoriesSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MovieDirectorViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    queryset = MovieDirector.objects.all()
    serializer_class = MovieDirectorSerializer
    # permission_classes = [permissions.IsAuthenticated]
