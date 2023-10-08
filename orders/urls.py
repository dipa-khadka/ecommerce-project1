from django.urls import path
import orders.views as views

urlpatterns = [
    path('cart', views.shopping_cart, name="cart_page"),
    path('checkout',views.checkout, name="checkout_page" ),
    path('order_summary',views.orders_summary, name="order_summary_page"),
   
]
