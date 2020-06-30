from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    try:
        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', {})
        if id in cart:
            cart[id] = int(cart[id]) + quantity
        else:
            cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    except ValueError:
        messages.error(request, "Quantity must be greater than zero")
        return redirect(reverse('works'))


def remove_from_cart(request, id):
    """Remove a specified product from the cart"""

    cart = request.session.get('cart', {})
    cart.pop(id, None)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
