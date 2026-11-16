from django import template

register = template.Library()

@register.filter
def transform_scientific_name(value):
    return value.title()

