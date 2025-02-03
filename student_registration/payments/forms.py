# payments/forms.py
from django import forms
from .models import Payment
from courses.models import Course


class PaymentForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True)

    class Meta:
        model = Payment
        fields = ["amount", "course"]
