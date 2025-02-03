# from django.urls import path
# from . import views
#
# urlpatterns = [
#    # path('pay/<int:registration_id>/', views.make_payment, name='make_payment'),
#     #path('payment_success/', views.payment_success, name='payment_success'),
#     #path('stripe-checkout/<int:payment_id>/', views.stripe_checkout, name='stripe_checkout'),
#     path('pay/', views.make_payment, name='make_payment'),
#     path('checkout/<int:payment_id>/', views.stripe_checkout, name='stripe_checkout'),
#     path('success/', views.payment_success, name='payment_success'),
#     path('failed/', views.payment_failed, name='payment_failed'),
# ]
# payments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("pay/", views.make_payment, name="make_payment"),
    path("success/", views.payment_success, name="payment_success"),
    path("failed/", views.payment_failed, name="payment_failed"),
]
