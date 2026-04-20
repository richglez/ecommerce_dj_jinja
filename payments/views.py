import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def create_payment_session(request, pedido_id):
    pedido = get_object_or_404("orders.Pedido", id=pedido_id, customer_id=request.user)
    
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": f"Pedido #{pedido.id}",
                    },
                    "unit_amount": int(pedido.total * 100),
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri("/payments/success/") + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri("/payments/cancel/"),
        metadata={"pedido_id": pedido.id, "user_id": request.user.id},
    )
    
    return render(request, "payments/checkout.html", {"session_id": session.id})


@login_required
def payment_success(request):
    session_id = request.GET.get("session_id")
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)
        payments = __import__("payments.models", fromlist=["Payment"]).Payment.objects.filter(
            stripe_payment_id=session.payment_intent
        )
        if payments.exists():
            payment = payments.first()
            payment.status = "completed"
            payment.save()
            pedido = payment.pedido
            pedido.status = "processing"
            pedido.save()
            messages.success(request, "Payment completed successfully!")
    return render(request, "payments/success.html")


@login_required
def payment_cancel(request):
    messages.error(request, "Payment was cancelled.")
    return redirect("cart")


@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get("stripe-signature")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)
    
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        Payment.objects.create(
            pedido_id=session.metadata["pedido_id"],
            user_id=session.metadata["user_id"],
            stripe_payment_id=session.payment_intent,
            amount=session.amount_total / 100,
            status="completed",
        )
    
    return HttpResponse(status=200)
