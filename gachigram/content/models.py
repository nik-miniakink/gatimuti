from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

from core.models import DateCreateUpdateModel


class Meme(DateCreateUpdateModel):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь, добавивший мем'
    )

    def __str__(self):
        return self.title


class Sticker(DateCreateUpdateModel):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь, добавивший стикерпак',
    )

    def __str__(self):
        return self.title
