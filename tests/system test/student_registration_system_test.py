from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from student_registration.models import Course, Enrollment
import stripe


class StudentRegistrationSystemTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.admin_user = User.objects.create_superuser(
            username="admin", password="adminpassword"
        )
        self.course = Course.objects.create(
            name="Django Basics", description="Learn Django"
        )

    def test_user_registration(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
                "email": "newuser@example.com",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_login(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.post(
            reverse("login"), {"username": "wronguser", "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid credentials")

    def test_user_logout(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    def test_course_enrollment(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("enroll"), {"course_id": self.course.id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Enrollment.objects.filter(user=self.user, course=self.course).exists()
        )

    def test_course_listing(self):
        response = self.client.get(reverse("course_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django Basics")

    def test_payment_processing(self):
        stripe.api_key = "your_test_api_key"
        payment_intent = stripe.PaymentIntent.create(
            amount=1000, currency="usd", payment_method_types=["card"]
        )
        self.assertTrue(
            payment_intent.status in ["requires_payment_method", "succeeded"]
        )

    def test_failed_payment_handling(self):
        stripe.api_key = "your_test_api_key"
        try:
            stripe.PaymentIntent.create(
                amount=-1000, currency="usd", payment_method_types=["card"]
            )
        except stripe.error.StripeError as e:
            self.assertIsNotNone(e)

    def test_dashboard_access(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_admin_access_control(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("admin:index"))
        self.assertNotEqual(
            response.status_code, 200
        )

        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
