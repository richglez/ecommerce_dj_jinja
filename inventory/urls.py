from django.urls import path
from . import views

urlpatterns = [
    path("admin/inventory/", views.inventory_list, name="admin_inventory_list"),
    path("admin/inventory/add/", views.inventory_add, name="admin_inventory_add"),
    path("admin/inventory/<int:product_id>/", views.inventory_detail, name="admin_inventory_detail"),
    path("admin/inventory/<int:product_id>/update/", views.inventory_update, name="admin_inventory_update"),
]