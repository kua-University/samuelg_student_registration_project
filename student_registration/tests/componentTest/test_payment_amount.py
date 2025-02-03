from django.test import TestCase
from student_registration_project.payments.forms import PaymentForm

class PaymentAmountValidationTest(TestCase):
    def test_valid_payment_amount(self):
        form = PaymentForm(data={'amount': 100.00, 'course': 1})
        self.assertTrue(form.is_valid())

    def test_invalid_payment_amount_zero(self):
        form = PaymentForm(data={'amount': 0, 'course': 1})
        self.assertFalse(form.is_valid())

    def test_invalid_payment_amount_negative(self):
        form = PaymentForm(data={'amount': -50, 'course': 1})
        self.assertFalse(form.is_valid())
