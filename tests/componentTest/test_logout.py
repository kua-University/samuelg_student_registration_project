from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
class LogoutTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertRedirects(response, reverse('login'))  # Ensure redirect to login
