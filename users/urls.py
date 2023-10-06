from django.urls import path
import users.views as views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('login/',views.user_login, name="login_page" ),
    path('register/',views.user_register, name="register_page")
   
]
