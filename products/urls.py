from django.urls import path
import products.views as views

urlpatterns = [
    path('new-arrival/', views.new_arrival_products, name="new-arrival_page"),
    path('product-detail/<int:product_id>',views.product_detail, name="product-detail_page" ),
    # path('register/',views.user_register, name="register_page")
   
]
