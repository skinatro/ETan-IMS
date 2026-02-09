from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Component, Order, OrderItem


class CustomerRegistrationForm(UserCreationForm):
    pid = forms.IntegerField(required=True, label="PID Number")
    phone_number = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "pid", "phone_number", "password1", "password2"]


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            "name",
            "category",
            "quantity",
            "is_rentable",
            "rental_rate",
            "product_image",
            "datasheet_url",
            "description",
            "location",
        ]


class OrderItemForm(forms.Form):
    component = forms.ModelChoiceField(
        queryset=Component.objects.filter(is_rentable=True, quantity__gt=0)
    )
    quantity = forms.IntegerField(min_value=1, initial=1)
