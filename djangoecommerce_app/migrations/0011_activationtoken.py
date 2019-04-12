# Generated by Django 2.0.9 on 2019-04-11 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoecommerce_app', '0010_auto_20190410_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(editable=False, max_length=256, verbose_name='Token')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yaratılma Tarihi')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Aktivasyon',
                'verbose_name_plural': 'Aktivasyonlar',
                'ordering': ('-created',),
            },
        ),
    ]