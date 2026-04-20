from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_orders, name="list_orders"),
    path("<int:pedido_id>/", views.detail_order, name="detail_order"),
    path("create/", views.create_order_from_cart, name="create_order"),
    path("<int:pedido_id>/<str:status>/", views.update_order_status, name="update_order_status"),
]