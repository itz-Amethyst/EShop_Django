from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic.base import TemplateView , View
from django.views.generic import ListView, DetailView

from .models import Product , ProductCategory , ProductBrand
from django.http import Http404 , HttpRequest
from django.db.models import Avg , Min , Max , Count


# Create your views here.

class ProductListView(ListView):
    template_name = 'Product_Module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-created_date']
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        print("Runned: Context_Data")
        context = super().get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        # db_min_price = query.order_by('price').first().price
        db_max_price = product.price if product is not None else 0

        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        # Can use this way but not dynamiced with db
        # context['end_price'] = self.request.GET.get('end_price') or Product.objects.aggregate(Max('price'))
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        return context

    def get_queryset(self):
        print("Runned: QuerySet")

        query = super().get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price != None:
            query = query.filter(price__gte = start_price)

        if end_price != None:
            query = query.filter(price__lte = end_price)

        if brand_name != None:
            query = query.filter(brand__url_title__iexact = brand_name)

        if category_name != None:
            query = query.filter(category__url_title__iexact = category_name)
        return query

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


def ProductCategories_Component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active = True,)
    context = {
        'categories': product_categories
    }

    return render(request, 'Product_Module/components/Product_Categories.html', context)


def ProductBrands_Component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(products_count=Count('product_brands')).filter(is_active = True) # annotate name must be related name relation in Model
    context = {
        'brands': product_brands
    }

    return render(request, 'Product_Module/components/Product_Brands.html', context)


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