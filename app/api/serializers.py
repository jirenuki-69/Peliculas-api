from .models import *
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'ranking', 'category']

    def to_representation(self, instance):
      ret = super().to_representation(instance)

      return {
        'id': ret['id'],
        'name': ret['name'],
        'description': ret['description'],
        'ranking': ret['ranking'],
        'category_id': ret['category']
      }

class MovieCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategories
        fields = ['id', 'name']

class ActorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Actor
    fields = ['name', 'genre']

class MovieActorSerializer(serializers.ModelSerializer):
  class Meta:
    model = MovieActor
    fields = ['actor', 'movie']
  
  def to_representation(self, instance):
      ret = super().to_representation(instance)

      return {
        'actor_id': ret['actor'],
        'movie_id': ret['movie']
      }

class DirectorSerializer(serializers.ModelSerializer):
  class Meta:
    model: Director
    fields = ['name']

class MovieDirectorSerializer(serializers.ModelSerializer):
  class Meta: 
    model = MovieDirector
    fields = ['director', 'movie']

  def to_representation(self, instance):
      ret = super().to_representation(instance)

      return {
        'director_id': ret['director'],
        'movie_id': ret['movie']
      }