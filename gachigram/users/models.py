from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserFavoriteContent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_actors = models.ManyToManyField(
        'actors.Actor', related_name='favorited_by', blank=True
    )
    favorite_memes = models.ManyToManyField(
        'memes.Meme', related_name='favorited_by', blank=True
    )
    favorite_movies = models.ManyToManyField(
        'movies.Movie', related_name='favorited_by', blank=True
    )
    favorite_stickers = models.ManyToManyField(
        'stickers.Sticker', related_name='favorited_by', blank=True
    )

    def __str__(self):
        return self.user.username
