import json
import os.path

from django.core.management import BaseCommand
from django.db import connection

from blog.models import Blog
from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def json_read():
        with open(
            os.path.join(BASE_DIR, "fixtures", "blog.json"), encoding="utf-8"
        ) as json_file:
            data = json.load(json_file)
        return data

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE blog_blog RESTART IDENTITY CASCADE;")

        Blog.objects.all().delete()

        blog = Command.json_read()

        blog_for_create = []

        for post in blog:
            blog_for_create.append(
                Blog(
                    title=post["fields"]["title"],
                    slug=post["fields"]["slug"],
                    content=post["fields"]["content"],
                    photo=post["fields"]["photo"],
                    created_at=post["fields"]["created_at"],
                    is_published=post["fields"]["is_published"],
                    view_count=post["fields"]["view_count"],
                )
            )

        Blog.objects.bulk_create(blog_for_create)
