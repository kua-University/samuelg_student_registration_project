from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class RegisterTest(TestCase):
    def test_register_valid_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login after registration
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())  # Check if user is created
