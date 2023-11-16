# Generated by Django 4.2.6 on 2023-11-16 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gender",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("slug", models.SlugField(unique=True, verbose_name="Идентификатор")),
            ],
        ),
        migrations.CreateModel(
            name="MovieGenres",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("slug", models.SlugField(unique=True, verbose_name="Идентификатор")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
            ],
        ),
        migrations.CreateModel(
            name="Nationalities",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("slug", models.SlugField(unique=True, verbose_name="Идентификатор")),
            ],
        ),
        migrations.AlterField(
            model_name="actor",
            name="gender",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="library.gender"
            ),
        ),
    ]