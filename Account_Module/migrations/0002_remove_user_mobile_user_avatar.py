# Generated by Django 4.2.4 on 2023-09-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_Module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='UserImages', verbose_name='تصویر کاربری'),
        ),
    ]
