# Generated by Django 4.1 on 2022-08-24 14:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("is_author", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Joke",
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
                ("joke", models.CharField(blank=True, max_length=255, unique=True)),
                ("answer", models.CharField(blank=True, max_length=255, unique=True)),
                (
                    "rate",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(5.0),
                        ]
                    ),
                ),
                ("vote_count", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="jokes.user"
                    ),
                ),
            ],
        ),
    ]