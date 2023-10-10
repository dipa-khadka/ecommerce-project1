from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Username" }),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}),
        }
    