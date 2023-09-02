from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Product_List, name='product-list'),
    path('', views.ProductListView.as_view(), name = 'product-list') ,
    path('<slug:product_slug>', views.ProductDetailView.as_view(), name='product-detail')
]