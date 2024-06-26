from django.urls import path, include
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ContactsView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryUpdateView,
    CategoryCreateView,
    CategoryDetailView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home_page"),
    path("contacts/", ContactsView.as_view(), name="contact_info"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_page"),
    path("category/<int:pk>/", cache_page(60)(CategoryDetailView.as_view()), name="category_page"),
    path("create_product/", ProductCreateView.as_view(), name="product_create"),
    path(
        "update_product/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "update_category/<int:pk>/",
        CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path("create_category/", CategoryCreateView.as_view(), name="category_create"),
]
