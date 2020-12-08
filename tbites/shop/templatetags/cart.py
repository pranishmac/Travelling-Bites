from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(item,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==item.id:
            return True
    return False
   
@register.filter(name='cart_quantity')
def cart_quantity(item,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==item.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(item,cart):
    return item.price * cart_quantity(item , cart)

@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0 
    for p in products:
        sum += price_total(p, cart)
    return sum

@register.filter(name='multiply')
def multiply(number,number1):
    return number*number1


   