# Generated by Django 4.2.4 on 2023-08-29 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='is_readed_by_admin',
            new_name='is_read_by_admin',
        ),
    ]
