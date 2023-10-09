from django.db import models
from products.models import Products
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(cart_product, on_delete=models.CASCADE)
    total_price = models.FloatField(max_length=200)
    cart_quantity = models.IntegerField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
# class Orders(models.Model):
    