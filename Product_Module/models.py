from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length = 300, db_index = True, verbose_name = "عنوان")
    url_title = models.CharField(max_length = 300, db_index = True, verbose_name = "عنوان در url")
    is_active = models.BooleanField(verbose_name = "فعال / غیرفعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    title = models.CharField(max_length = 200)

    category = models.ManyToManyField(
        ProductCategory,
        related_name = 'product_categories',
        verbose_name ='دسته بندی ها') # models.PROTECT , models.SET_NULL
    price = models.IntegerField(verbose_name = "قیمت")

    # rating = models.IntegerField(
    #     validators = [MinValueValidator(1), MaxValueValidator(5)], default = 0
    # )

    short_description = models.CharField(max_length = 360, db_index = True, null = True, verbose_name = "توضیحات کوتاه")
    description = models.TextField(verbose_name = "توضیحات تکمیلی")
    is_active = models.BooleanField(default = False, verbose_name = "فعال / غیرفعال")
    slug = models.SlugField(default = "", null = False, db_index = True, blank = True, unique = True )#*, editable = False*# cant use with prepopulated_fields in admin
    is_deleted = models.BooleanField(verbose_name = "حذف شده / نشده") ## Same as Is active IDK Why he added
    created_date = models.DateTimeField(verbose_name = "تاریخ ساخت" , default = datetime.now)

    def get_products_tags( self ):
        return "\n - ".join([p.tag for p in self.product_tags.all()])
    def get_product_categories( self ):
        return "\n - ".join([p.title for p in self.category.all()])

    def get_absolute_url( self ):
        return reverse('product-detail', args = [self.slug])

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

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption