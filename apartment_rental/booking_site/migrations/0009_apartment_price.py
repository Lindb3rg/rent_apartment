# Generated by Django 5.1 on 2024-09-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_site', '0008_alter_apartment_accessible_alter_apartment_heating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
