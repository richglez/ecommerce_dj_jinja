from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test


def staff_member_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        from django.shortcuts import redirect
        return redirect("signin")
    return wrapper
from products.models import Product
from .models import Inventory


@staff_member_required
def inventory_list(request):
    inventories = Inventory.objects.select_related("product").all()
    return render(request, "admin/inventory_list.html", {"inventories": inventories})


@staff_member_required
def inventory_detail(request, product_id):
    inventory = get_object_or_404(Inventory.objects.select_related("product"), product_id=product_id)
    return render(request, "admin/inventory_detail.html", {"inventory": inventory})


@staff_member_required
def inventory_add(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        quantity = request.POST.get("quantity", 0)
        location = request.POST.get("location", "")
        Inventory.objects.update_or_create(
            product=product,
            defaults={"quantity": quantity, "location": location}
        )
        return redirect("admin_inventory_list")
    products = Product.objects.filter(inventory__isnull=True)
    return render(request, "admin/inventory_form.html", {"products": products})


@staff_member_required
def inventory_update(request, product_id):
    inventory = get_object_or_404(Inventory.objects.select_related("product"), product_id=product_id)
    if request.method == "POST":
        inventory.quantity = request.POST.get("quantity", inventory.quantity)
        inventory.location = request.POST.get("location", inventory.location)
        inventory.save()
        return redirect("admin_inventory_list")
    return render(request, "admin/inventory_form.html", {"inventory": inventory})