from django.shortcuts import render
from djangoecommerce_web.serializers.homepage import ProductListSerializer
from djangoecommerce_app.models import User, City, CompanyAddress, CompanyFeature,Card,Order, Company, ProductCategory,  Product, ProductImage, ProductBrand


def IndexView(request):
    context={
        "product":ProductListSerializer(Product.objects.all(), many=True).data
    }
    return render(request, 'web/index.html',context)
