from django.contrib import admin
from catalog.models import Category, Product, Contacts


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
