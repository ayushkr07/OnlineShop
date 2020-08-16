from django import template

register = template.Library()


@register.filter(name='rupee')
def add_rupee_sign(value):
    return f'₹{value}'


@register.filter(name='discounted_price')
def discounted_price(product):
    return product.price - (product.price * product.discount) / 100
