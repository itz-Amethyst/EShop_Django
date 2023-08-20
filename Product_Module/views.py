from django.shortcuts import render , get_object_or_404
from .models import Product
from django.http import Http404

# Create your views here.

def Product_List(request):
    products = Product.objects.all()
    return render(request, "Product_Module/product_list.html",{
        'products': products
    })

def Product_Detail(request, product_id):
    # try:
    #     product = Product.objects.get(id = product_id)
    # except:
    #     raise Http404()

    ## Same as Top
    product = get_object_or_404(Product, pk = product_id)

    return render(request, "Product_Module/product_details.html",{
        'product': product
    })