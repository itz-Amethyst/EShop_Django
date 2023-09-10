from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    # mobile = models.CharField(max_length = 15, verbose_name = "تلفن همراه", null = True)
    avatar = models.ImageField(upload_to = 'UserImages', verbose_name = 'تصویر کاربری', null = True, blank = True)
    email_active_code = models.CharField(max_length = 100, verbose_name = "کد فعال سازی ایمیل")

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if (self.get_full_name() != None):
            return self.get_full_name()

        return self.email


