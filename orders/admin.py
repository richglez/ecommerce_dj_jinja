from django.contrib import admin
from .models import Pedido, PedidoItem


class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 0
    readonly_fields = ["product", "quantity", "price", "subtotal"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "total", "status", "date"]
    list_filter = ["status", "date"]
    search_fields = ["customer__username", "id"]
    inlines = [PedidoItemInline]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(PedidoItem)
class PedidoItemAdmin(admin.ModelAdmin):
    list_display = ["pedido", "product", "quantity", "price", "subtotal"]
    search_fields = ["pedido__id", "product__name"]
