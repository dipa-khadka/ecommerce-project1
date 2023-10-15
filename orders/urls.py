from django.urls import path
import orders.views as views

urlpatterns = [
    path('cart/', views.shopping_cart, name="cart_page"),
    path('checkout/',views.checkout, name="checkout_page" ),
    path('order-summary/',views.order_summary, name="order_summary_page"),
    path('add-to-cart/<int:product_id/',views.add_to_cart, name="add_to_cart_page")
   
]
