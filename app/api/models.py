from django.db import models

class MovieCategories(models.Model):
  name = models.CharField(max_length=500)

class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    ranking = models.IntegerField(1)
    category = models.ForeignKey(MovieCategories, on_delete=models.PROTECT)

class Actor(models.Model):
  name = models.CharField(max_length=250)
  genre = models.CharField(max_length=1)

class MovieActor(models.Model):
  actor = models.ForeignKey(Actor, on_delete=models.PROTECT)
  movie = models.ForeignKey(Movie, on_delete=models.PROTECT)

class Director(models.Model):
  name = models.CharField(max_length=250)

class MovieDirector(models.Model):
  director = models.ForeignKey(Director, on_delete=models.PROTECT)
  movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
