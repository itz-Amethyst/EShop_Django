from django.http import HttpRequest

from Product_Module.models import ProductVisit , Product
from Site_Module.models import SiteBanner


def SelectSiteBanner( choice ):
    return SiteBanner.objects.filter(is_active = True , position__iexact = choice)


def Group_List( custom_list , size = 4 ):
    grouped_list = []
    group_size = size

    for i in range(0 , len(custom_list) , size):
        grouped_list.append(custom_list[i:i + size])
    return grouped_list


def get_client_ip( request: HttpRequest ):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def handle_ip_in_ProductVisit(request: HttpRequest, object ):
    user_ip_address = get_client_ip(request)
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    # print(user_ip_address)

    has_been_visited = ProductVisit.objects.filter(ip__exact = user_id).exists()
    if not has_been_visited:
        new_visit = ProductVisit(ip = user_id, user_id = user_id, product_id = object.id)
        new_visit.save()


def handle_ip_in_Product_item_visit_count(request: HttpRequest, object ):
    user_ip_address = get_client_ip(request)
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    # print(user_ip_address)

    has_been_visited = ProductVisit.objects.filter(ip__exact = user_id).exists()
    if not has_been_visited:
        new_visit = ProductVisit(ip = user_id, user_id = user_id, product_id = object.id)
        new_visit.save()
        item: Product = Product.objects.filter(id = object.id).first()
        item.item_visit_count += 1

