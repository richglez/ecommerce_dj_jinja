from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    pedido = models.ForeignKey(
        "orders.Pedido", on_delete=models.CASCADE, related_name="payments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_payment_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.stripe_payment_id} - {self.status}"
