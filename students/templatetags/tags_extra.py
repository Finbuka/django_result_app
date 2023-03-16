from django import template

register = template.Library()

@register.filter
def divide(value, arg):
    try:
        var_divided = value/arg
    except Exception as e:
        var_divided = 0
    return var_divided

@register.simple_tag
def define(value=None):
    return value

@register.filter
def additon(value, arg):
    return value + arg
