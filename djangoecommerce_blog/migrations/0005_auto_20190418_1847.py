# Generated by Django 2.1.8 on 2019-04-18 15:47

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoecommerce_blog', '0004_auto_20190418_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='color',
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='category_color',
            field=colorfield.fields.ColorField(default='#fe4c50', max_length=18),
        ),
    ]
