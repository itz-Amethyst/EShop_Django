# Generated by Django 4.2.4 on 2023-10-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order_Module', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='final_price',
            new_name='final_price_per_item',
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت نهایی سبد'),
        ),
    ]
