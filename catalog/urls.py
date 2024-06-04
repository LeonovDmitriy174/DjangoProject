from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ContactsView,
    ProductUpdateView,
    ProductDeleteView,
)


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home_page"),
    path("contacts/", ContactsView.as_view(), name="contact_info"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_page"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
