from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    is_main_setting = models.BooleanField(verbose_name = 'تنظیمات اصلی سایت')
    site_name = models.CharField(max_length = 200, verbose_name = 'نام سایت')
    site_url = models.CharField(max_length = 200, verbose_name = 'دامنه سایت')
    address = models.CharField(max_length = 200, verbose_name = 'ادرس')
    phone = models.CharField(max_length = 200, null = True, blank = True, verbose_name = 'تلفن')
    fax = models.CharField(max_length = 200, null = True, blank = True, verbose_name = 'فکس')
    email = models.CharField(max_length = 200, null = True, blank = True, verbose_name = 'ایمیل')
    site_logo = models.ImageField(upload_to = 'images/site-settings/' , verbose_name = 'لوگو سایت')
    copy_right = models.TextField(verbose_name = 'متن کپی رایت سایت')
    about_us_text = models.TextField(max_length = 200, verbose_name = 'متن درباره ما سایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__( self ):
        return self.site_name