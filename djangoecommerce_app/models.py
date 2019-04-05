from django.db import models
from django.db.models import Model,ForeignKey,CharField,DateTimeField,FloatField

from django.contrib.auth.models import AbstractUser


STATUS=(
    ('Musteri','Müşteri'),
    ('Sirket','Şirket'),
)

class User(AbstractUser):
    user_status = CharField(max_length=15, verbose_name="Kullanıcı Durumu",choices=STATUS)

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Tüm Kullanıcılar'