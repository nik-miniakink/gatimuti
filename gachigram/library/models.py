from django.contrib.auth import get_user_model
from django.db import models

from .utils import genders, movie_genres, nationalities
from core.models import DateCreateUpdateModel

User = get_user_model()


class Actor(DateCreateUpdateModel):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255, blank=True)
    scenic_name = models.CharField('Сценическое имя', max_length=255, blank=True)
    birthdate = models.DateField('День рождения', null=True, blank=True)
    gender = models.CharField('Пол', max_length=255, blank=True, choices=genders)
    nationality = models.CharField(
        'Национальность', max_length=255, blank=True, choices=nationalities
    )
    biography = models.TextField('Биография', null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь, добавивший актёра'
    )
    movies = models.ManyToManyField('Movie', related_name='actors')
    memes = models.ManyToManyField('content.Meme', related_name='actors')
    stickers = models.ManyToManyField('content.Sticker', related_name='actors')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(DateCreateUpdateModel):
    title = models.CharField('Название', max_length=255)
    release_date = models.DateField('Дата выхода', null=True, blank=True)
    director = models.CharField('Режиссёр', max_length=255, blank=True)
    genre = models.CharField('Жанр', max_length=255, blank=True, choices=movie_genres)
    description = models.TextField('Описание', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь, добавивший фильм'
    )

    def __str__(self):
        return self.title
