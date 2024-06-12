from django.db import models
from django.db.models import DateField, BooleanField
from django.utils import timezone

from users.models import User


# Create your models here.
class Category(models.Model):

    def __str__(self):
        return f"{self.name}"

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
        return f"{self.name}"

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
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Создан пользователем",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену товара")
    created_at = DateField(
        verbose_name="Дата создания записи",
        help_text="Укажите дату создания",
        default=timezone.now,
    )
    updated_at = DateField(
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
        default=timezone.now,
    )
    is_published = BooleanField(
        verbose_name="Опубликовано", help_text="Признак публикации", default=False
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at", "-updated_at", "name", "price", "category"]
        permissions = [
            ("change_published", "Может менять признак публикации продукта"),
            ("change_description", "Может менять описание продукта"),
            ("change_category", "Может менять категорию продукта"),
        ]


class Contacts(models.Model):

    def __str__(self):
        return self.country

    country = models.CharField(
        max_length=100, verbose_name="Страна", help_text="Введите страну"
    )
    INN = models.CharField(
        max_length=100,
        verbose_name="ИНН",
        help_text="Введите ИНН",
    )
    address = models.TextField(
        verbose_name="Адрес отделения", help_text="Введите адрес отделения"
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = [
            "country",
        ]


class Version(models.Model):

    def __str__(self):
        return f"{self.product} - {self.number_version} ({self.name_version})"

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="version",
        verbose_name="Продукт",
        help_text="Введите продукт",
    )
    number_version = models.PositiveIntegerField(
        verbose_name="Номер версии", help_text="Введите номер версии"
    )
    name_version = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Активная ли версия",
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ["product", "number_version", "name_version"]
