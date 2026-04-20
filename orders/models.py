from django.db import models
from django.contrib.auth.models import User


# User (1) -> Pedido (n)
class Pedido(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)
