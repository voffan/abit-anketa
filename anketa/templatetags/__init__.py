from django import template

register = template.Library()

def as_bootstrap_div(value): # Only one argument.
    """Converts a field into a control inside a bootstrap container"""
    return value.lower()