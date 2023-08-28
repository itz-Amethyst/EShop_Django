from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    # Same as generate slug in c# but here is a note it cant be worked with readonly fields of that value
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['__str__', 'price', 'is_active' ,'get_product_categories' , 'get_products_tags']
    list_filter = ['is_active']
    list_editable = ['is_active']
class Product_category_admin(admin.ModelAdmin):
    list_display = ['__str__','url_title']
    list_editable = ['url_title']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, Product_category_admin)
admin.site.register(models.ProductTag)
