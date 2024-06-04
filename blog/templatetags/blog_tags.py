from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"


@register.filter()
def description_hundred(description):
    return description[:100] + "..."


@register.filter()
def is_published(object_list):
    new_object_list = []
    for obj in object_list:
        if obj.is_published:
            new_object_list.append(obj)
    return new_object_list
