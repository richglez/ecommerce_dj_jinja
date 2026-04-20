from django.urls import path
from . import views

urlpatterns = [
    path("create/<int:pedido_id>/", views.create_payment_session, name="create_payment"),
    path("success/", views.payment_success, name="payment_success"),
    path("cancel/", views.payment_cancel, name="payment_cancel"),
    path("webhook/", views.stripe_webhook, name="stripe_webhook"),
]