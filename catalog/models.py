from django.db import models
from django.db.models import DateField


# Create your models here.
class Category(models.Model):

    def __str__(self):
        return f"Категория: \n{self.name}\n" f"Описание: \n{self.description}"

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):

    def __str__(self):
        return (
            f"Продукт: \n{self.name}\n"
            f"Цена: {self.price}\n"
            f"Описание: \n{self.description}"
        )

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию товара",
        null=True,
        blank=True,
        related_name="categories",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену товара")
    created_at = DateField(
        verbose_name="Дата создания записи", help_text="Укажите дату создания"
    )
    updated_at = DateField(
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at", "-updated_at", "name", "price", "category"]
