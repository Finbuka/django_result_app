from django import template

register = template.Library()

@register.filter
def divide(value, arg):
    return value/arg

@register.simple_tag
def define(value=None):
    return value

@register.filter
def additon(value, arg):
    return value + arg
