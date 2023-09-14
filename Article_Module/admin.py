from django.contrib import admin
from . import models
from .models import Article


# Register your models here.
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'parent', 'is_active']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'make_short_description_shorter', 'is_active', 'get_selected_categories', 'author']
    list_editable = ['is_active']

    def save_model(self, request, obj: Article, form, change):

        print('change:', change)
        print('object:', obj)
        print('user:', request.user)

        if not change:
            #? Note only change author in create page or action not in edit f.e created by milad edited by reza but author still is milad
            obj.author = request.user

        # obj.author = request.user
        return super().save_model(request, obj, form, change)
    #! Note in admin it will display the name of def
    def make_short_description_shorter( self, obj ):
        return obj.short_description[:65]


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)