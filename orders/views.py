from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Pedido, PedidoItem
from cart.models import Cart
from products.models import Product


@login_required
def list_orders(request):
    pedidos = Pedido.objects.filter(customer=request.user).order_by("-date")
    return render(request, "orders/list.html", {"pedidos": pedidos})


@login_required
def detail_order(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, customer=request.user)
    items = pedido.items.all()
    for item in items:
        item.subtotal = item.quantity * item.price
    return render(request, "orders/detail.html", {"pedido": pedido, "items": items})


@login_required
@transaction.atomic
def create_order_from_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.select_related("product")

    if not items.exists():
        return redirect("cart")

    total = sum(item.product.price * item.quantity for item in items)

    pedido = Pedido.objects.create(
        customer=request.user,
        total=total,
        status="pending"
    )

    for item in items:
        PedidoItem.objects.create(
            pedido=pedido,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart.items.all().delete()

    return redirect("detail_order", pedido_id=pedido.id)


@login_required
def update_order_status(request, pedido_id, status):
    pedido = get_object_or_404(Pedido, id=pedido_id, customer=request.user)
    if status in ["pending", "processing", "shipped", "delivered", "cancelled"]:
        pedido.status = status
        pedido.save()
    return redirect("detail_order", pedido_id=pedido.id)