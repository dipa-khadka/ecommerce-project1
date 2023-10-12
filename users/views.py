from django.shortcuts import render,redirect
from users.forms import  UserRegisterForm
from users.models import User,Profile
from django.contrib import messages
from django.contrib.auth import  authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, template_name="index.html")


def user_login(request):
    return render(request, "login.html")
 
def user_register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form_data = UserRegisterForm(request.POST)
        if form_data.is_valid():
            print("Form Data: ", form_data.cleaned_data)
            password = form_data.cleaned_data["password"]
            confirm_password = form_data.cleaned_data["confirm_password"]
            if password != confirm_password:
                error = "Password and Confirm Password fields does not match"
                messages.error(request, error)
                return redirect("/register")
            check_user = User.objects.filter(username=form_data.cleaned_data["username"]).exists()
            check_email = User.objects.filter(email=form_data.cleaned_data["email"]).exists()
            if check_user or check_email:
                error = "Username or Email already exists"
                messages.error(request, error)
                return redirect("/register")
            user_account_data = {
                "first_name": form_data.cleaned_data["first_name"],
                "last_name": form_data.cleaned_data["last_name"],
                "username": form_data.cleaned_data["username"],
                "email": form_data.cleaned_data["email"],
            }
            user = User.objects.create(**user_account_data)
            user.set_password(password)
            user.save()
            profile_data = {
                "user": user,
                "contact": form_data.cleaned_data["contact"],
                "address": form_data.cleaned_data["address"],
                "city": form_data.cleaned_data["city"],
                "profile_pic": "N/A"
            }
            profile = profile.objects.create(**profile_data)
        return redirect("/login")
    return render(request, "register.html", {"form": form})


@login_required
def user_profile(request):
    # equivalent sql: SELECT * FROM profile WHERE user_id=1
    # get profile of user with id user_id
    Profile = Profile .objects.get(user_id=user_id)
    context = {"Profile": Profile}
    return render(request, "profile.html")

def user_logout(request):
    logout(request)
    return redirect("/login")
    
    


