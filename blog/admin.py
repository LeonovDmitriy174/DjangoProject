from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "content", "photo", "created_at", "is_published", "view_count")
    search_fields = ("title", "content")
    list_filter = ("created_at", "view_count",)