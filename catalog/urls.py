from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home_page, contact_info


app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home_page'),
    path('contacts/', contact_info, name='contact_info')
]
