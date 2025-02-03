from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User  # Link to the custom User model
        fields = ['username', 'email', 'is_student', 'is_admin']  # Add fields as per your needs
