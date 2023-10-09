from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order', views.Add_Product_To_Order, name='add_product_to_order'),
    path('request-payment/', views.Request_Payment, name='request_Payment'),
    path('verify-payment/', views.Verify_Payment, name='verify_Payment')
]