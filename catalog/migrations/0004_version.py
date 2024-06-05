# Generated by Django 5.0.6 on 2024-06-05 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_created_at_alter_product_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                    "number_version",
                    models.PositiveIntegerField(
                        help_text="Введите номер версии", verbose_name="Номер версии"
                    ),
                ),
                (
                    "name_version",
                    models.CharField(
                        help_text="Введите название версии",
                        max_length=100,
                        verbose_name="Название версии",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False, verbose_name="Активная ли версия"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="Введите продукт",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="version",
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия продукта",
                "verbose_name_plural": "Версии продуктов",
                "ordering": ["product", "number_version", "name_version"],
            },
        ),
    ]
