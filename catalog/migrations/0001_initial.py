# Generated by Django 5.0.6 on 2024-05-08 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Наименование категории",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "name",
                    models.CharField(
                        help_text="Введите наименование продукта",
                        max_length=100,
                        verbose_name="Наименование продукта",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание продукта",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение продукта",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Введите цену товара", verbose_name="Цена"
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        help_text="Укажите дату создания",
                        verbose_name="Дата создания записи",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        help_text="Укажите дату последнего изменения",
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию товара",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="categories",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["-created_at", "-updated_at", "name", "price", "category"],
            },
        ),
    ]
