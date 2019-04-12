# Generated by Django 2.1.8 on 2019-04-12 16:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoecommerce_app', '0010_auto_20190410_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Ürün Fiyatı'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False, verbose_name='Onaylandı'),
        ),
    ]
