from django.contrib import admin
from .models import Product

# Registra el model exclusivamente para herramientas de gestión interna y personal de soporte.
admin.site.register(Product)
