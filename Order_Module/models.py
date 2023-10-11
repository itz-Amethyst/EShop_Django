from django.db import models
from Account_Module.models import User
from Product_Module.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, verbose_name = 'کاربر')
    is_paid = models.BooleanField(verbose_name = 'نهایی شده / نشده', default = False)
    payment_date = models.DateField(null = True, blank = True, verbose_name = 'تاریخ پرداخت')
    total_price = models.IntegerField(null = True, blank = True, verbose_name = 'قیمت نهایی سبد')
    # can add total price here

    # def calculate_total_price(self):
    #     total_amount = 0
    #     if self.is_paid:
    #         for order_detail in self.orderdetail_set.all():
    #             total_amount += order_detail.final_price * order_detail.count
    #     else:
    #         for order_detail in self.orderdetail_set.all():
    #             total_amount += order_detail.product.price * order_detail.count
    #
    #     return total_amount

    def calculate_total_price(self, product_id = None, flag=False):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price_per_item * order_detail.count
        elif flag:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count
        elif product_id:
            for order_detail in self.orderdetail_set.filter(product_id = product_id):
                total_amount = order_detail.product.price

        return total_amount


    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        # in user model __str__ func will return
        return str(self.user)


class OrderDetail(models.Model):
    product = models.ForeignKey(to = Product, on_delete = models.CASCADE, verbose_name = 'محصول')
    order = models.ForeignKey(to = Order, on_delete = models.CASCADE, verbose_name = 'سبد خرید')
    final_price_per_item = models.IntegerField(null = True, blank = True, verbose_name = 'قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name = 'تعداد محصول')

    # def get_total_price( self ):
    #     return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جرئیات سبد خرید'
        verbose_name_plural = 'لیست جزئیات سبدهای خرید'