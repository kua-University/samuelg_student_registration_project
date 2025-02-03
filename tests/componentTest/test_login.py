from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
class LoginTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')
    def test_login_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('course_list'))
