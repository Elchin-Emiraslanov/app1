from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string

from carts.models import Cart
from carts.templatetags.carts_tags import user_carts
from carts.utils import get_user_carts
from goods.models import Products


def cart_add(request):

    product_id = request.POST.get("product_id")

    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Product is added to basket",
        "cart_items_html": cart_items_html
    }

    return JsonResponse(response_data)

def cart_change(request):
    if request.method == "POST":
        cart_id = request.POST.get("cart_id")
        quantity = request.POST.get("quantity")

        print(f"Received cart_id: {cart_id}, quantity: {quantity}")

        cart = Cart.objects.get(id=cart_id)
        cart.quantity = quantity
        cart.save()
        updated_quantity = cart.quantity

        user_cart = get_user_carts(request)
        cart_items_html = render_to_string(
            "carts/includes/included_cart.html", {"carts": user_cart}, request=request
        )

        response_data = {
            "message": "Quantity changed",
            "cart_items_html": cart_items_html,
            "quantity": updated_quantity
        }

        print("Response data:", response_data)

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)



def cart_remove(request):
    
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)

    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message" : "Product removed",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)