# Generated by Django 5.1 on 2024-09-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_site', '0007_apartment_contact_person_apartment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='accessible',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='heating',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='kitchen',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='shower',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='tv',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='wifi',
            field=models.CharField(max_length=50),
        ),
    ]
