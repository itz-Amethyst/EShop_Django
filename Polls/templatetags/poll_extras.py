from django import template
from jalali_date import date2jalali

register = template.Library()

@register.filter(name = 'show_jalali_date')
def show_jalali_date(value):
    return date2jalali(value)

@register.filter(name = 'show_jalali_time')
def show_jalali_time(value):
    return value.strftime('%H:%M')

@register.filter(name = 'three_digits_divide_currency')
def three_digits_divide_currency(value: int):
    return '{:,}'.format(value) + 'تومان'

@register.simple_tag
def multiply_price_checkout(quantity, price, *args, **kwargs):
    return three_digits_divide_currency(quantity * price)


