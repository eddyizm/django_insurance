# Generated by Django 5.0.2 on 2024-07-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drivers',
            new_name='Driver',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='Drivers',
            new_name='Driver',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='Vehicles',
            new_name='Vehicle',
        ),
        migrations.AlterField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]