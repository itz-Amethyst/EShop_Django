from django.urls import path
from . import views

urlpatterns = [
    path('', views.Product_List, name='product-list'),
    path('<slug:product_slug>', views.Product_Detail, name='product-detail')
]