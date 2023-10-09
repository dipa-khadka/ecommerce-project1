from django.urls import path
import products.views as views

urlpatterns = [
    path('new-arrival/', views.new_arrival_product, name="new_arrival_page"),
    path('product/<int:product_id>/',views.product_detail, name="product_detail_page" ),
    # path('register/',views.user_register, name="register_page")
   
]
