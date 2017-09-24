from django import template

from menu.models import Item, Menu

register = template.Library()

@register.filter
def dict(dict, value):
    try:
        return dict[value]
    except:
        return False

@register.simple_tag
def next (path):
    return path[0]

@register.simple_tag
def path (path):
    return path[1:]
