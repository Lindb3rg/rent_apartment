# Generated by Django 5.1 on 2024-09-14 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_site', '0005_rename_street_name_apartment_street_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='address',
        ),
    ]
