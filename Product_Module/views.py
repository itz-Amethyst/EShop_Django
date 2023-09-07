from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic.base import TemplateView , View
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.

class ProductListView(ListView):
    template_name = 'Product_Module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-created_date']
    paginate_by = 12

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(is_active = True)
    #     return data

    # def get_context_data( self , **kwargs ):
    #     context = super().get_context_data()
    #     slug = kwargs['slug']
    #     product = get_object_or_404(Product, slug = slug)
    #     context['product'] = product
    #     return context

class ProductDetailView(DetailView):
    template_name = 'Product_Module/product_details.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get('product_favorites')
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context

    # def get_context_data(self, **kwargs):
    #     products = Product.objects.all().order_by('-price')[5]
    #     context = super().get_context_data()
    #     context['products'] = products
    #     return context

class AddProductFavoriteView(View):
    def post( self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk = product_id)
        request.session["product_favorites"] = product_id
        return redirect(product.get_absolute_url())


# def Product_List(request):
#     # console = ProductCategory(title = "پلی استیشن", url_title = "playstation")
#     # console.save()
#     #
#     # ps_4 = Product(title = 'Ps5', price = 25000000, category = console, short_description = "play station 5 console", rating = 4, is_active = True)
#     # ps_4.save()
#
#
#     products = Product.objects.all().order_by('-price')[:5] # if we add - , will order by descending
#     # number_of_products = products.count()
#     # avg_rating = products.aggregate(Avg('rating'))
#     # min_price = products.aggregate(Min('price'))
#     # max_price = products.aggregate(Max('price'))
#
#     return render(request, "Product_Module/product_list.html",{
#         'products': products,
#         # 'total_number_of_products': number_of_products,
#         # 'average_rating': avg_rating,
#         # 'min_price': min_price,
#         # 'max_price': max_price
#     })


# def Product_Detail(request, product_slug):
#     # try:
#     #     product = Product.objects.get(id = product_id)
#     # except:
#     #     raise Http404()
#
#     ## Same as Top
#     product = get_object_or_404(Product, slug = product_slug)
#
#     return render(request, "Product_Module/product_details.html",{
#         'product': product
#     })