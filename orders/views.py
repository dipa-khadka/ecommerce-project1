from django.shortcuts import render

# Create your views here.
def shopping_cart(request):
    return render(request, "carts.html")


def checkout(request):
    return render(request, "checkout.html")

def order_summary(requeust):
    return render(requeust, "orders.html")


