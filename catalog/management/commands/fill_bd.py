import datetime
import json
import os.path

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def json_read():
        with open(os.path.join(BASE_DIR, 'fixtures', 'catalog.json'), encoding='utf-8') as json_file:
            data = json.load(json_file)

            list_categories = []
            list_products = []
            for i in data:
                if i['model'] == 'catalog.product':
                    list_products.append(i)
                else:
                    list_categories.append(i)

        return list_categories, list_products

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        Category.objects.all().delete()
        Product.objects.all().delete()

        categories, products = Command.json_read()

        product_for_create = []
        category_for_create = []

        for category in categories:
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description']))

        Category.objects.bulk_create(category_for_create)

        for product in products:
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        photo=product['fields']['photo'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=datetime.datetime.now().date()))

        Product.objects.bulk_create(product_for_create)