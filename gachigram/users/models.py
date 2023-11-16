from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import DateCreateUpdateModel


class User(AbstractUser):
    pass


class UserFavoriteContent(DateCreateUpdateModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    favorite_actors = models.ManyToManyField(
        'library.Actor',
        related_name='favorited_by',
        blank=True,
        verbose_name='Любимые актеры',
    )
    favorite_memes = models.ManyToManyField(
        'content.Meme',
        related_name='favorited_by',
        blank=True,
        verbose_name='Любимые мемы',
    )
    favorite_movies = models.ManyToManyField(
        'library.Movie',
        related_name='favorited_by',
        blank=True,
        verbose_name='Любимые фильмы',
    )
    favorite_stickers = models.ManyToManyField(
        'content.Sticker',
        related_name='favorited_by',
        blank=True,
        verbose_name='Любимые стикеры',
    )

    def __str__(self):
        return str(self.user)
