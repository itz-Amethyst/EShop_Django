from django.contrib import admin
from . import models


# Register your models here.
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'parent', 'is_active']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'make_short_description_shorter', 'is_active', 'get_selected_categories']
    list_editable = ['is_active']

    # Note in admin it will display the name of def
    def make_short_description_shorter( self, obj ):
        return obj.short_description[:65]


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)