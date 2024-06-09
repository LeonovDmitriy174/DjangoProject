# Generated by Django 5.0.6 on 2024-06-04 04:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "content",
                    models.TextField(
                        help_text="Введите содержание", verbose_name="Содержание"
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение продукта",
                        null=True,
                        upload_to="blog/photo",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        default=django.utils.timezone.now,
                        help_text="Укажите дату создания",
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True,
                        help_text="Признак публикации",
                        verbose_name="Опубликовано",
                    ),
                ),
                (
                    "view_count",
                    models.IntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блог",
            },
        ),
    ]