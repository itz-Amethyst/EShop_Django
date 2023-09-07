from django.urls import path , re_path
from . import views

urlpatterns = [
    # path('', views.Product_List, name='product-list'),
    path('', views.ProductListView.as_view(), name = 'product-list') ,
    path('product_favorite', views.AddProductFavoriteView.as_view() , name = 'product-favorite') ,
    # path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    # re_path(r'products/(?P<slug>[-\w]+)/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]