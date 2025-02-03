from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class PaymentProcessingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="TestPassword123")
        self.client.login(username="testuser", password="TestPassword123")

    def test_payment_process(self):
        response = self.client.post(reverse('make_payment'), {
            'course': 1,  # Assuming course with ID 1 exists
            'amount': 100.00
        })
        self.assertEqual(response.status_code, 302)  # Redirect to Stripe
        self.assertTrue(Payment.objects.exists())

    def test_payment_failure(self):
        response = self.client.post(reverse('make_payment'), {
            'course': 1,
            'amount': -100.00  # Invalid amount
        })
        self.assertNotEqual(response.status_code, 302)  # Should not redirect
