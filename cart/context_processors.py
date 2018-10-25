from .cart import Cart


def cart(request):          #The context processor is so that the cart is available to all templates
    return {'cart': Cart(request)}