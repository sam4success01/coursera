# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='proper_case')
def proper_case(value):
    """Converts a string to proper/title case."""
    return value.title() if isinstance(value, str) else value
