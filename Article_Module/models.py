from django.db import models
from django.utils.text import slugify
from jalali_date import date2jalali

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
    created_date = models.DateTimeField(auto_now_add = True, editable = False, verbose_name = 'تاریخ ایجاد')

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

    #! Another way to declare custom functions but its better to be added in polls custom tags

    # def get_jalali_create_date(self):
    #     return date2jalali(self.created_date)
    #
    #
    # def get_jalali_create_time(self):
    #     return self.created_date.strftime('%H:%M')

class ArticleComment(models.Model):
    article = models.ForeignKey(to = Article, on_delete = models.CASCADE, verbose_name = 'مقاله')
    parent = models.ForeignKey(to = 'ArticleComment', on_delete = models.CASCADE, null = True, blank = True,  verbose_name = 'والد')
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, verbose_name = 'کاربر')
    create_date = models.DateTimeField(auto_now_add = True, verbose_name = 'تاریخ ثبت')
    text = models.TextField(verbose_name = 'متن نظر')
    is_submitted = models.BooleanField(default = False, verbose_name = 'تایید شده / نشده')

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقالات'