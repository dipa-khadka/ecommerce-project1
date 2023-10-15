from django.shortcuts import render
from orders.models import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def shopping_cart(request):
    carts = Cart.objects.filter(user=request.user).order_by("created_at")
    context = {"carts": carts}
    return render(request, "carts.html", context)



@login_required
def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart_data= {
        "user": request.user,
        "product": product,
        "cart_qty": 1,
        "cart_total": product.price
    }
    Cart.objects.create(**cart_data)
    return redirect("/cart")
    


def checkout(request):
    return render(request, "checkout.html")

def order_summary(requeust):
    return render(requeust, "orders.html")


