# Generated by Django 4.2.4 on 2023-09-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_Module', '0005_sitebanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitebanner',
            name='position',
            field=models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزيیات محصولات'), ('about_us', 'درباره ما')], max_length=200, verbose_name='جایگاه نمایشی'),
        ),
    ]
