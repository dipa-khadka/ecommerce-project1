from django.urls import path
import users.views as views

urlpatterns = [
    path('', views.home, name="home_page"),
]
