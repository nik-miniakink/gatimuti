from django.contrib.auth import get_user_model
from django.db import models

from core.models import DateCreateUpdateModel

User = get_user_model()


class Gender(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Идентификатор', unique=True)

    def __str__(self):
        return self.title


class MovieGenres(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title


class Nationalities(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Идентификатор', unique=True)

    def __str__(self):
        return self.title


class Actor(DateCreateUpdateModel):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255, blank=True)
    scenic_name = models.CharField('Сценическое имя', max_length=255, blank=True)
    birthdate = models.DateField('День рождения', null=True, blank=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пол'
    )
    nationality = models.ForeignKey(
        Nationalities,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Национальность',
    )
    biography = models.TextField('Биография', null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь, добавивший актёра'
    )
    movies = models.ManyToManyField(
        'Movie', related_name='actors', blank=True, verbose_name='Фильмы'
    )
    memes = models.ManyToManyField(
        'content.Meme', related_name='actors', blank=True, verbose_name='Мемы'
    )
    stickers = models.ManyToManyField(
        'content.Sticker', related_name='actors', blank=True, verbose_name='Стикеры'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(DateCreateUpdateModel):
    title = models.CharField('Название', max_length=255)
    release_date = models.DateField('Дата выхода', null=True, blank=True)
    director = models.CharField('Режиссёр', max_length=255, blank=True)
    genre = models.ManyToManyField(
        MovieGenres,
        blank=True,
        related_name='movies',
        verbose_name='Жанры',
    )
    description = models.TextField('Описание', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь, добавивший фильм'
    )

    def __str__(self):
        return self.title
