from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    # mobile = models.CharField(max_length = 15, verbose_name = "تلفن همراه", null = True)
    avatar = models.ImageField(upload_to = 'images/UserImages', verbose_name = 'تصویر کاربری', null = True, blank = True)
    email_active_code = models.CharField(max_length = 100, verbose_name = "کد فعال سازی ایمیل")
    about_user = models.TextField(null = True, blank = True, verbose_name = 'درباره شخص')
    address = models.TextField(null = True, blank = True, verbose_name = 'ادرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        #! Have 2 way to fix this 1 by this long or change it inside a get_full_name method
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()

        return self.email


