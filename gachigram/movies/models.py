from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода')
    director = models.CharField(max_length=255, blank=True, verbose_name='Режиссёр')
    genre = models.CharField(max_length=255, blank=True, verbose_name='Жанр')
    description = models.TextField(blank=True, verbose_name='Описание')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь, добавивший фильм'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    def __str__(self):
        return self.title
