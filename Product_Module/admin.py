from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    # Same as generate slug in c# but here is a note it cant be worked with readonly fields of that value
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(models.Product, ProductAdmin)