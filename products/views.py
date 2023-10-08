from django.shortcuts import render

# Create your views here.

def new_arrival_product(request):
    return render(request, "new-arrival.html")


def product_detail(request, product_id):
    return render(request, "product-detail.html")