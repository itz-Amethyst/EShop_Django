from django.db.models import Count
from django.http import HttpRequest

from Order_Module.models import Order
from Product_Module.models import ProductVisit , Product , ProductCategory
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


def handle_ip_in_ProductVisit( request: HttpRequest , object ):
    user_ip_address = get_client_ip(request)
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    # print(user_ip_address)

    has_been_visited = ProductVisit.objects.filter(ip__exact = user_ip_address , product_id = object.id).exists()
    if not has_been_visited:
        new_visit = ProductVisit(ip = user_ip_address , user_id = user_id , product_id = object.id)
        new_visit.save()


def handle_ip_in_Product_item_visit_count( request: HttpRequest , object ):
    user_ip_address = get_client_ip(request)
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    # print(user_ip_address)

    has_been_visited = ProductVisit.objects.filter(ip__exact = user_ip_address , product_id = object.id).exists()
    if not has_been_visited:
        new_visit = ProductVisit(ip = user_ip_address , user_id = user_id , product_id = object.id)
        new_visit.save()
        item: Product = Product.objects.filter(id = object.id).first()
        item.item_visit_count += 1


def Get_Categories_With_Products():
    # ! Note when you put query inside list will run immediately otherwise not
    categories = list(ProductCategory.objects.annotate(products_count = Count('product_categories')).filter(is_active = True, products_count__gt = 0)[:6])
    categories_product = []
    for category in categories:
        item = {
            'id': category.id,
            'title': category.title,
            'products': list(category.product_categories.all()[:4])
        }
        categories_product.append(item)
    return categories_product


def Get_CurrentOrder_And_Price(request: HttpRequest, flag=False):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid = False, user_id = request.user.id)
    total_amount = current_order.calculate_total_price(flag = True)

    return current_order, total_amount