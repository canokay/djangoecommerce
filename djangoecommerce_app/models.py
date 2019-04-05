from django.db import models
from django.db.models import Model,ForeignKey,CharField,DateTimeField,FloatField,EmailField,ImageField,DateField,TextField, BooleanField

from django.contrib.auth.models import AbstractUser


STATUS=(
    ('Musteri','Müşteri'),
    ('Sirket','Şirket'),
)

class User(AbstractUser):
    GENDERS = (
        ('Erkek', 'Erkek'),
        ('Kadın', 'Kadın'),
        ('Belirtilmemiş', 'Belirtilmemiş'),
    )
    user_status = CharField(max_length=15, verbose_name="Kullanıcı Durumu",choices=STATUS)
    profile_photo = ImageField(verbose_name='Profil Fotoğrafı', upload_to='images/user/profile/', blank=True, null=True)
    gender = CharField(max_length=100, null=True, blank=True, verbose_name='Cinsiyet', choices=GENDERS)
    birthday = DateField(null=True, blank=True, verbose_name='Doğum Tarihi')
    bio = TextField(blank=True, null=True, verbose_name='Biyografi')
    phone = CharField(max_length=100, null=True, blank=True, verbose_name='Telefon No')
    is_verified = BooleanField(blank=True, default=True, verbose_name='Onaylandı')

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Tüm Kullanıcılar'