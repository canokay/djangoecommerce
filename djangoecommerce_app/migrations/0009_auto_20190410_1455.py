# Generated by Django 2.0.9 on 2019-04-10 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoecommerce_app', '0008_auto_20190409_0112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-transaction_time',), 'verbose_name': 'Satın Alım', 'verbose_name_plural': 'Satın Alımlar'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ('-id',), 'verbose_name': 'Ürün Resmi', 'verbose_name_plural': 'Ürün Resimleri'},
        ),
        migrations.AlterModelOptions(
            name='productstar',
            options={'ordering': ('-id',), 'verbose_name': 'Ürün Yıldızı', 'verbose_name_plural': 'Ürün Yıldızları'},
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='owner',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='djangoecommerce_app.ProductBrand', verbose_name='Ürün Markası'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/product/', verbose_name='Resimi'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='images/product/', verbose_name='Resim'),
        ),
    ]