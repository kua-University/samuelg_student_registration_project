from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from payments.models import Payment


class IntegrationTestCase(TestCase):
    def test_full_user_flow(self):
        # Register User
        self.client.post(
            reverse("register"),
            {
                "username": "testuser",
                "password1": "TestPassword123",
                "password2": "TestPassword123",
            },
        )

        # Login User
        self.client.post(
            reverse("login"), {"username": "testuser", "password": "TestPassword123"}
        )

        # Make Payment
        response = self.client.post(
            reverse("make_payment"),
            {"course": 1, "amount": 100.00},  # Assuming course with ID 1 exists
        )
        self.assertEqual(response.status_code, 200)  # Redirect to Stripe Checkout
        self.assertTrue(Payment.objects.exists())

        # Logout
        self.client.get(reverse("logout"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)
