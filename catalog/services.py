from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    else:
        key = "products"
        products = cache.get(key)
        if products is not None:
            return products
        else:
            products = Product.objects.all()
            cache.set(key, products)
            return products
