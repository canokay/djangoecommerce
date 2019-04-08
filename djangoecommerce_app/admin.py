from django.contrib import admin
from django.contrib.auth.models import Group
from djangoecommerce_app.models import User, City, CompanyAddress, CompanyFeature, Company, ProductCategory,  Product, ProductImage, ProductBrand


admin.site.register(User)
admin.site.register(City)
admin.site.register(CompanyAddress)
admin.site.register(CompanyFeature)
admin.site.register(Company)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductBrand)

admin.site.unregister(Group)
