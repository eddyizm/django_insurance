# Generated by Django 5.0.7 on 2024-08-19 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0007_alter_driver_quote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='quote_id',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='quote_id',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
