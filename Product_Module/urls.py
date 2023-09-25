from django.urls import path , re_path
from . import views

urlpatterns = [
    # path('', views.Product_List, name='product-list'),
    path('', views.ProductListView.as_view(), name = 'product-list'),
    path('cat/<cat>', views.ProductListView.as_view(), name = 'product-categories-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name = 'products-brand-list'),
    path('product_favorite', views.AddProductFavoriteView.as_view(), name = 'product-favorite'),
    # path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    # re_path(r'products/(?P<slug>[-\w]+)/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),

]