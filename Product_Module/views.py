from django.shortcuts import render
from .models import Product

# Create your views here.

def Product_List(request):
    products = Product.objects.all()
    return render(request, "Product_Module/product_list.html",{
        'products': products
    })