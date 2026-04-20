from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Un carrito
class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )  # permite carritos para usuarios no logueados
    session_key = models.CharField(
        max_length=40, null=True, blank=True
    )  # Identifica carritos de usuarios anónimos usando sesión de cookies
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def total(self):
        total = sum(item.subtotal() for item in self.items.all())
        return total

    def __str__(self):
        return f"Cart {self.id}"


# Cart (1) - CartItem (n)
# CartItem (1) - Product (1)


# Los productos dentro del carrito
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"


# -Summary Diagram Relation
# Cart
#   (1)
#   └── CartItem (n)
#          └── Product (1)
