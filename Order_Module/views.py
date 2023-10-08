from django.http import HttpRequest , HttpResponse , JsonResponse
from django.shortcuts import render

from Order_Module.models import Order , OrderDetail
from Product_Module.models import Product
from utils.ZarinPal import Send_Request, Verify


# Create your views here.

def Add_Product_To_Order( request: HttpRequest ):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        # count = 1
        return JsonResponse({
            'status': 'invalid_count' ,
            'text': 'مقدار وارد شده معتبر نمیباشد' ,
            'confirm_button_text': 'باشه فهمیدم' ,
            'icon': 'warning'
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id = product_id , is_active = True , is_deleted = False).first()

        if product != None:

            # Cause its return tuple [any , bool]
            current_order , created = Order.objects.get_or_create(is_paid = False , user_id = request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id = product_id).first()
            if current_order_detail != None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id = current_order.id , product_id = product_id , count = count)
                new_detail.save()

            return JsonResponse({
                'status': 'success' ,
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد' ,
                'confirm_button_text': 'باشه ممنون' ,
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found' ,
                'text': 'محصول مورد نظر یافت نشد' ,
                'confirm_button_text': 'OK' ,
                'icon': 'warning'
            })

    else:
        return JsonResponse({
            'status': 'not_auth' ,
            'text': 'برای افزودن محصول به سبد خرید باید وارد سایت شوید' ,
            'confirm_button_text': 'باشه گرفتم' ,
            'icon': 'error'
        })


def Request_Payment( request: HttpRequest ):
    Send_Request(request)


def Verify_Payment(request: HttpRequest):
    t_authority = request.GET['Authority']
    Verify(t_authority)
