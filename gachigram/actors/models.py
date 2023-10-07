from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Actor(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, blank=True, verbose_name='Фамилия')
    birthdate = models.DateField(null=True, blank=True, verbose_name='День рождения')
    gender = models.CharField(max_length=1, blank=True, verbose_name='Пол')
    nationality = models.CharField(
        max_length=255, blank=True, verbose_name='Национальность'
    )
    biography = models.TextField(null=True, blank=True, verbose_name='Биография')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь, добавивший актёра',
    )
    movies = models.ManyToManyField('movies.Movie', related_name='actors')
    memes = models.ManyToManyField('memes.Meme', related_name='actors')
    stickers = models.ManyToManyField('stickers.Sticker', related_name='actors')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
