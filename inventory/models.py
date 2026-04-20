from django.db import models
from products.models import Product


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="inventory")
    quantity = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"