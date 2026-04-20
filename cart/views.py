from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if session_key:
            cart, created = Cart.objects.get_or_create(session_key=session_key)
        else:
            request.session.create()
            session_key = request.session.session_key
            cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


def cart_view(request):
    cart = get_or_create_cart(request)
    items = cart.items.all()
    total = cart.total()

    return render(request, "cart.html", {"cart": cart, "items": items, "total": total})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart = get_or_create_cart(request)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product, defaults={"quantity": 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)

    CartItem.objects.filter(cart=cart, product=product).delete()

    return redirect("cart")


def update_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)

    quantity = int(request.POST.get("quantity", 1))
    if quantity > 0:
        CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity)
    else:
        CartItem.objects.filter(cart=cart, product=product).delete()

    return redirect("cart")