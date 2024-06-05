from django.db import models
from django.db.models import DateField, BooleanField
from django.utils import timezone


class Blog(models.Model):

    def __str__(self):
        return f"{self.title}"

    title = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    slug = models.SlugField(unique=True, verbose_name="Слаг", help_text="Введите слаг")
    content = models.TextField(
        verbose_name="Содержание", help_text="Введите содержание"
    )
    photo = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    created_at = DateField(
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        default=timezone.now,
    )
    is_published = BooleanField(
        verbose_name="Опубликовано", help_text="Признак публикации", default=True
    )
    view_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров", default=0
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
