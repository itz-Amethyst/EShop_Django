from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order', views.Add_Product_To_Order, name='add_product_to_order')
]