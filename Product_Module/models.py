from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

from Account_Module.models import User


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length = 300, db_index = True, verbose_name = "عنوان")
    url_title = models.CharField(max_length = 300, db_index = True, verbose_name = "عنوان در url")
    is_active = models.BooleanField(verbose_name = "فعال / غیرفعال")
    #? Implement paretn later if you want

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class ProductBrand(models.Model):
    title = models.CharField(max_length = 300, verbose_name = "نام برند", db_index = True)
    url_title = models.CharField(max_length = 300, verbose_name = "نام برند در url", db_index = True)
    is_active = models.BooleanField(default = False, verbose_name = "فعال / غیر فعال")

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "نام محصول")

    category = models.ManyToManyField(
        ProductCategory,
        related_name = 'product_categories',
        verbose_name ='دسته بندی ها') # models.PROTECT , models.SET_NULL
    image = models.ImageField(upload_to = 'images/products', null = True, blank = True, verbose_name = 'تصویر محصول')

    brand = models.ForeignKey(ProductBrand, on_delete = models.CASCADE,verbose_name = "برند", related_name = "product_brands", null = True, blank = True) ## blank = true will accept null or empty
    price = models.IntegerField(verbose_name = "قیمت")

    # rating = models.IntegerField(
    #     validators = [MinValueValidator(1), MaxValueValidator(5)], default = 0
    # )

    short_description = models.CharField(max_length = 360, db_index = True, null = True, verbose_name = "توضیحات کوتاه")
    description = models.TextField(verbose_name = "توضیحات تکمیلی")
    is_active = models.BooleanField(default = False, verbose_name = "فعال / غیرفعال")
    slug = models.SlugField(default = "", null = False, db_index = True, blank = True, unique = True, verbose_name = "عنوان در Url" )#*, editable = False*# cant use with prepopulated_fields in admin
    is_deleted = models.BooleanField(verbose_name = "حذف شده / نشده") ## Same as Is active IDK Why he added
    created_date = models.DateTimeField(verbose_name = "تاریخ ساخت" ,auto_now_add = True)

    #! Another way for ProductVisit
    item_visit_count = models.IntegerField(null = True, blank = True, verbose_name = 'تعداد بازدید محصول')

    def get_products_tags( self ):
        return "\n - ".join([p.caption for p in self.product_tags.all()])
    def get_product_categories( self ):
        return "\n - ".join([p.title for p in self.category.all()])
    def get_absolute_url( self ):
        return reverse('product-detail', kwargs = {'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length = 200, db_index = True, verbose_name = "عنوان")

    product = models.ForeignKey(Product , verbose_name = "تگ های محصول" , related_name = 'product_tags', on_delete = models.CASCADE)

    def get_tag_products( self ):
        return "\n - ".join([p.product.title for p in self.product.product_tags.all()])

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption

class ProductVisit(models.Model):
    product = models.ForeignKey(to = Product, on_delete = models.CASCADE, verbose_name = 'محصول')
    ip = models.GenericIPAddressField(max_length = 30, verbose_name = 'آی پی کاربر')
    user = models.ForeignKey(to = User, null = True, blank = True, verbose_name = 'کاربر مشاهده گر', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدیدهای محصول'