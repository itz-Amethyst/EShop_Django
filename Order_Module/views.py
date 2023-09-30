from django.http import HttpRequest , HttpResponse , JsonResponse
from django.shortcuts import render

from Order_Module.models import Order , OrderDetail
from Product_Module.models import Product


# Create your views here.

def Add_Product_To_Order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active = True, is_deleted = False).first()

        if product != None:

            # Cause its return tuple [any , bool]
            current_order, created = Order.objects.get_or_create(is_paid = False, user_id = request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id = product_id).first()
            if current_order_detail != None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id = current_order.id, product_id = product_id, count = count)
                new_detail.save()

            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found'
            })

    else:
        return JsonResponse({
            'status': 'User is not authenticated'
        })