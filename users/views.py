from django.shortcuts import render
from users.forms import  UserRegisterForm

# Create your views here.
def home(request):
    return render(request, template_name="index.html")


def user_login(request):
    return render(request, "login.html")
 
def user_register(request):
    form = UserRegisterForm()
    return render(request, "register.html", {"form": form})

def user_profile(request):
    return render(request, "profile.html")

