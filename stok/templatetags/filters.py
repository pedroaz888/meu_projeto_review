from django import template

register = template.Library()

@register.filter
def br_money(value):
    if value is None:
        return ''
    return f"{value:,.2f}".replace(',', 'temp').replace('.', ',').replace('temp', '.')