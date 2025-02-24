import pytest
from django.urls import reverse
from unittest.mock import patch
from users.models import User  # Use custom User model

@pytest.mark.django_db
def test_registration_and_payment(client):
    # Test User Registration
    response = client.post(reverse('register'), {
        'username': 'newuser',
        'password1': 'strongpassword',
        'password2': 'strongpassword',
    })
    assert response.status_code == 302  # Expecting a redirect
    assert response.url == reverse('login')  # Redirect after successful registration
    assert User.objects.filter(username='newuser').exists()

    # Force Login for Payment Test
    user = User.objects.get(username='newuser')
    client.force_login(user)

    # Mock Stripe Checkout Session
    with patch('stripe.checkout.Session.create') as mock_session:
        mock_session.return_value = type('obj', (object,), {"id": "sess_12345", "url": "https://checkout.stripe.com/pay/test"})
        response = client.post(reverse('make_payment'), {'course': 1, 'amount': 10})
        assert response.status_code == 302  # Expecting a redirect to Stripe Checkout
        assert "https://checkout.stripe.com/pay/test" in response.url  # Mocked URL
        mock_session.assert_called_once()
