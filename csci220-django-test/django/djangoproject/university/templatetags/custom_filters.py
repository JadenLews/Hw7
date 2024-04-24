from django import template

register = template.Library()

@register.filter
def reformat(value):
    return value.replace('_',' ').title()