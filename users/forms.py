from django import forms
from django.contrib.auth.models import User


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password']
#         widgets = {
#             "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name"}),
#             "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name"}),
#             "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Username" }),
#             "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}),
#             "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}),
#         }
        
      
class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TimeInput(
        attrs={"class": "form-control", "placeholder": "Enter First Name"}
    ))
    
    last_name = forms.CharField(max_length=100, widget=forms.TimeInput(
        attrs={"class": "form-control", "placeholder": "Enter Last Name"}
    ))
    
    username = forms.CharField(max_length=100, widget=forms.TimeInput(
        attrs={"class": "form-control", "placeholder": "Enter Username"}
    ))
    
    email= forms.CharField(max_length=100, widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "Enter Email"}
    ))
    
      
    city = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter City"}
    ))
    
    
    address= forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter contact"}
    ))
    
      
    contact = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Repeat your  Password"}
    ))
    
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter Password"}
    ))
    
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Repeat your  Password"}
    ))
    