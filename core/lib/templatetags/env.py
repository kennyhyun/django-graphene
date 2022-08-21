import os
from django import template

register = template.Library()

@register.simple_tag
def getenv(key, default=None):
    return os.environ.get(key, default)
