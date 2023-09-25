# Generated by Django 4.2.4 on 2023-09-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_Module', '0004_slider_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان بنر')),
                ('url', models.URLField(blank=True, max_length=400, null=True, verbose_name='آدرس بنر')),
                ('image', models.ImageField(upload_to='images/banners', verbose_name='تصویر بنر')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیر فعال')),
                ('position', models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('proudct_detail', 'صفحه جزيیات محصولات'), ('about_us', 'درباره ما')], max_length=200, verbose_name='جایگاه نمایشی')),
            ],
            options={
                'verbose_name': 'بنر تبلیغاتی',
                'verbose_name_plural': 'بنرهای تبلیغاتی',
            },
        ),
    ]
