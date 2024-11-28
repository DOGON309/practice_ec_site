from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """値を指定された引数で掛け算するカスタムフィルター"""
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0
