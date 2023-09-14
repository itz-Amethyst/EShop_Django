from django.db import models
from django.utils.text import slugify

from Account_Module.models import User


# Create your models here.

class ArticleCategory(models.Model):
    parent = models.ForeignKey(to = 'ArticleCategory', null = True, blank = True, on_delete = models.CASCADE, verbose_name = 'دسته بندی والد')
    title = models.CharField(max_length = 200, verbose_name = 'عنوان دسته بندی')
    url_title = models.CharField(max_length = 200, verbose_name = 'عنوان در url', unique = True) # Unique_for_month har mah ye data unique darim
    is_active = models.BooleanField(verbose_name = 'فعال / غیرفعال', default = True)

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'عنوان مقاله')
    slug = models.SlugField(max_length = 400, db_index = True, allow_unicode = True, verbose_name = 'عنوان در url')
    image = models.ImageField(upload_to = 'images/articles', verbose_name = 'تصویر مقاله')
    short_description = models.TextField(verbose_name = 'توضیحات کوتاه')
    text = models.TextField(verbose_name = 'متن مقاله')
    is_active = models.BooleanField(default = True, verbose_name = 'فعال / غیرفعال')
    selected_categories = models.ManyToManyField(to = ArticleCategory, verbose_name = 'دسته بندی ها')
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, verbose_name = 'نویسنده', null = True, editable = False)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_selected_categories(self):
        return "\n - ".join([p.title for p in self.selected_categories.all()])

    def save( self , *args , **kwargs ):
        self.slug = slugify(self.title)
        super().save(*args , **kwargs)

    def __str__(self):
        return self.title
