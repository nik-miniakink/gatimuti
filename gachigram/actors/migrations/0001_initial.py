# Generated by Django 4.2.6 on 2023-10-07 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Фамилия"
                    ),
                ),
                (
                    "birthdate",
                    models.DateField(
                        blank=True, null=True, verbose_name="День рождения"
                    ),
                ),
                (
                    "gender",
                    models.CharField(blank=True, max_length=1, verbose_name="Пол"),
                ),
                (
                    "nationality",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Национальность"
                    ),
                ),
                (
                    "biography",
                    models.TextField(blank=True, null=True, verbose_name="Биография"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлён"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь, добавивший актёра",
                    ),
                ),
                (
                    "movies",
                    models.ManyToManyField(related_name="actors", to="movies.movie"),
                ),
            ],
        ),
    ]
