from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    # Same as generate slug in c# but here is a note it cant be worked with readonly fields of that value
    prepopulated_fields = {
        'slug': ['title']
    }

    exclude = ['created_date']

    # readonly_fields = ['created_date']
    list_display = ['__str__', 'price', 'is_active' ,'get_product_categories' , 'get_products_tags']
    list_filter = ['title', 'category', 'is_active']
    list_editable = ['is_active']
class Product_category_admin(admin.ModelAdmin):
    list_display = ['__str__','url_title']
    list_editable = ['url_title']

class Product_Tags_admin(admin.ModelAdmin):
    list_display = ['__str__', 'get_tag_products']

class Product_brand_admin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, Product_category_admin)
admin.site.register(models.ProductTag, Product_Tags_admin)
admin.site.register(models.ProductBrand, Product_brand_admin)
admin.site.register(models.ProductVisit)
