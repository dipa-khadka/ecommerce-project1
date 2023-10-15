from django.shortcuts import render
from products.models import Products

# Create your views here.

def new_arrival_product(request):
    return render(request, "new-arrival.html")


def product_detail(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {"product" : product}
    return render(request, "product-detail.html" ,context)