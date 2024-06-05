from django.contrib import admin
from catalog.models import Category, Product, Contacts, Version


# Register your models here.
@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "INN", "address")
    search_fields = ("country", "address")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "number_version", "name_version", "is_active")
    search_fields = ("product", "version")
