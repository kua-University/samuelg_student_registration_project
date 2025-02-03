from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from .models import Payment
from registration.models import Registration
from .forms import PaymentForm
import stripe

# Set up Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


def make_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data["course"]
            amount = form.cleaned_data["amount"]
            student = request.user  # Assume the logged-in user is the student

            # Ensure a registration exists
            registration, created = Registration.objects.get_or_create(
                student=student, course=course
            )

            # Create a payment record
            payment = Payment.objects.create(
                registration=registration, amount=amount, status="Pending"
            )

            # Create a Stripe Checkout Session
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": course.name,
                            },
                            "unit_amount": int(amount * 100),  # Convert to cents
                        },
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url=request.build_absolute_uri(reverse("payment_success"))
                + "?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=request.build_absolute_uri(reverse("payment_failed")),
                metadata={"payment_id": payment.id},
            )

            # Store the Stripe session ID in the payment record
            payment.stripe_payment_intent_id = session.id
            payment.save()

            # Redirect to Stripe Checkout
            return redirect(session.url)
    else:
        form = PaymentForm()

    return render(request, "payments/make_payment.html", {"form": form})


def payment_success(request):
    return render(request, "payments/payment_success.html")


def payment_failed(request):
    return render(request, "payments/payment_failed.html")
