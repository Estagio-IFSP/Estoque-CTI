from django import template

register = template.Library()

@register.filter
def to_verbose_name(object):
    return object._meta.verbose_name
