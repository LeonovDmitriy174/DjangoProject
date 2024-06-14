from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"


@register.filter()
def description_hundred(description):
    return description[:100] + "..."


@register.filter(name="has_group")
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter()
def category_list(product_list):
    category = []
    category_for_save = []
    for product in product_list:
        if product.category not in category:
            category.append(product.category)
            category_for_save.append(product)
    return set(category_for_save)
