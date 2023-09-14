from django.db import models

# Create your models here.

class ArticleCategory(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'عنوان دسته بندی')
    url_title = models.CharField(max_length = 200, verbose_name = 'عنوان در url', unique = True) # Unique_for_month har mah ye data unique darim
    is_active = models.BooleanField(verbose_name = 'فعال / غیرفعال', default = True)

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'

    def __str__(self):
        return self.title