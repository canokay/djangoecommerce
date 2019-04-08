from django.db import models
from django.db.models import Model,ForeignKey,CharField,DateTimeField,FloatField,EmailField,ImageField,DateField,TextField, BooleanField,IntegerField,DecimalField,ManyToManyField

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDERS = (
        ('Erkek', 'Erkek'),
        ('Kadın', 'Kadın'),
        ('Belirtilmemiş', 'Belirtilmemiş'),
    )
    profile_photo = ImageField(verbose_name='Profil Fotoğrafı', upload_to='images/user/profile/', blank=True, null=True)
    gender = CharField(max_length=100, null=True, blank=True, verbose_name='Cinsiyet', choices=GENDERS)
    birthday = DateField(null=True, blank=True, verbose_name='Doğum Tarihi')
    bio = TextField(blank=True, null=True, verbose_name='Biyografi')
    phone = CharField(max_length=100, null=True, blank=True, verbose_name='Telefon No')
    is_verified = BooleanField(blank=True, default=False, verbose_name='Onaylandı')

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Tüm Kullanıcılar'


class City(Model):
    name = CharField(max_length=255, verbose_name='İsim')
    number = IntegerField(verbose_name='İl Kodu', unique=True)

    class Meta:
        ordering = ('-number',)
        verbose_name = 'Şehir'
        verbose_name_plural = 'Şehirler'

    def __str__(self):
        return self.name


class CompanyAddress(Model):
    name = CharField(max_length=255, verbose_name='İsim', default='Adres', blank=True)
    open_address = TextField(max_length=100, verbose_name='Açık Adres')
    short_address = TextField(max_length=70, verbose_name='Kısa Adres')
    postal_code = CharField(max_length=10, null=True, blank=True, verbose_name='Posta Kodu')
    lat = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='X Koordinatı')
    long = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Y Koordinatı')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Adres'
        verbose_name_plural = 'Adresler'

    def __str__(self):
        return self.name



class CompanyFeature(Model):
    name = CharField(max_length=255, verbose_name='İsim')
    description = TextField(max_length=1000, verbose_name='Açıklama', blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Reklamveren Özelliği'
        verbose_name_plural = 'Reklamveren Özellikleri'

    def __str__(self):
        return self.name



class Company(User):
    city = ForeignKey('djangoecommerce_app.City', blank=True, null=True, verbose_name='Şehir', on_delete=models.CASCADE)
    address = ForeignKey('djangoecommerce_app.CompanyAddress', blank=True, null=True, verbose_name='Adres', on_delete=models.CASCADE)
    identity_number = CharField(max_length=11, null=True, blank=True, verbose_name='TC No')
    executive_namesurname = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Adı Soyadı')
    executive_identity_number = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili TC No')
    executive_email = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Email')
    executive_phone = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Telefon Numarası')
    mersis_no = CharField(max_length=250, null=True, blank=True, verbose_name='Mersis Numarası')
    kep_address = CharField(max_length=250, null=True, blank=True, verbose_name='Kep Adresi')
    tax_office = CharField(max_length=250, null=True, blank=True, verbose_name='Vergi Dairesi')
    tax_number = CharField(max_length=250, null=True, blank=True, verbose_name='Vergi No')
    legal_company_title = CharField(max_length=250, null=True, blank=True, verbose_name='Yasal Şirket Ünvanı')
    iban = CharField(max_length=250, null=True, blank=True, verbose_name='IBAN')
    link_facebook = CharField(max_length=250, null=True, blank=True, verbose_name='Facebook Linki')
    link_instagram = CharField(max_length=250, null=True, blank=True, verbose_name='Instagram Linki')
    link_twitter = CharField(max_length=250, null=True, blank=True, verbose_name='Twitter Linki')
    link_web = CharField(max_length=250, null=True, blank=True, verbose_name='Website Linki')
    features = ManyToManyField('djangoecommerce_app.CompanyFeature', verbose_name='Reklamveren Şirket Özellikleri', blank=True)

    class Meta:
        verbose_name = 'Şirket'
        verbose_name_plural = 'Şirketler'


class ProductCategory(Model):
    category = CharField(max_length=255, verbose_name='Ürün Kategorisi')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün Kategorisi'
        verbose_name_plural = 'Ürün Kategorileri'

    def __str__(self):
        return self.category


class ProductSubCategory(Model):
    owner = ForeignKey('djangoecommerce_app.ProductCategory', related_name='maincategory',blank=False, null=False, verbose_name='Ana Kategori', on_delete=models.CASCADE)
    sub_category = CharField(max_length=255, verbose_name='Ürün Kategorisi')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün Alt Kategorisi'
        verbose_name_plural = 'Ürün Alt Kategorileri'

    def __str__(self):
        return self.category


class ProductBrand(Model):
    name = CharField(max_length=255, verbose_name='Ürün Markası')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün Markası'
        verbose_name_plural = 'Ürün Markaları'

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255, verbose_name='Ürün Adı')
    description = TextField(max_length=1000, verbose_name='Açıklama')
    created_at = DateTimeField(auto_now_add=True, editable=False, blank=True, null=False,verbose_name='Oluşturma Tarihi')
    category = ForeignKey('djangoecommerce_app.ProductCategory', blank=True, null=True, verbose_name='Ürün Tipi', on_delete=models.CASCADE)
    owner = ForeignKey('djangoecommerce_app.User', related_name='owner',blank=False, null=False, verbose_name='Ürün Sahibi', on_delete=models.CASCADE)
    brand = ForeignKey('djangoecommerce_app.ProductBrand', related_name='brand',blank=False, null=False, verbose_name='Ürün Markası', on_delete=models.CASCADE)
    thumbnail = ImageField(verbose_name='İsim', upload_to='images/product/')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.name


class ProductImage(Model):
    image = ImageField(verbose_name='İsim', upload_to='images/product/')
    product = ForeignKey('djangoecommerce_app.Product', verbose_name='Sofra', null=True, blank=True, on_delete=models.CASCADE)
    owner = ForeignKey('djangoecommerce_app.Company', verbose_name='Sahibi', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Ürün Resmi'
        verbose_name_plural = 'Ürün Resimleri'

    def __str__(self):
        return self.image.name


class ProductStar(Model):
    product = ForeignKey('djangoecommerce_app.Product', verbose_name='Sofra', null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Ürün Resmi'
        verbose_name_plural = 'Ürün Resimleri'

    def __str__(self):
        return self.image.name
        verbose_name = 'Reklamveren'
        verbose_name_plural = 'Reklamverenler'
