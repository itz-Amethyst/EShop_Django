from django.shortcuts import render , get_object_or_404
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.

def Product_List(request):
    # console = ProductCategory(title = "پلی استیشن", url_title = "playstation")
    # console.save()
    #
    # ps_4 = Product(title = 'Ps5', price = 25000000, category = console, short_description = "play station 5 console", rating = 4, is_active = True)
    # ps_4.save()


    products = Product.objects.all().order_by('-price') # if we add - , will order by descending
    number_of_products = products.count()
    # avg_rating = products.aggregate(Avg('rating'))
    min_price = products.aggregate(Min('price'))
    max_price = products.aggregate(Max('price'))

    return render(request, "Product_Module/product_list.html",{
        'products': products,
        'total_number_of_products': number_of_products,
        # 'average_rating': avg_rating,
        'min_price': min_price,
        'max_price': max_price
    })

def Product_Detail(request, product_slug):
    # try:
    #     product = Product.objects.get(id = product_id)
    # except:
    #     raise Http404()

    ## Same as Top
    product = get_object_or_404(Product, slug = product_slug)

    return render(request, "Product_Module/product_details.html",{
        'product': product
    })