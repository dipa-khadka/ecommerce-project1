from django.db import models
from products.models import Products
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    total_price = models.FloatField(max_length=200)
    cart_quantity = models.IntegerField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
class Orders(models.Model):
     ORDER_STATUS = [("PENDING", "PENDING"), ("DELIVERED", "DELIVERED"), ("ON_THE_WAY", "ON_THE_WAY"), ("CANCELLED", "CANCELLED")]
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     Products = models.JSONField()
     total = models.FloatField(default=0)
     shipping_address = models.CharField(max_length=100)
     city = models.CharField(max_length=50)
     additional_info = models.CharField(max_length=100)
     payment_method = models.CharField(max_length=20, default="COD")
     status = models.CharField(max_length=30, choices=ORDER_STATUS, default="PENDING")
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     