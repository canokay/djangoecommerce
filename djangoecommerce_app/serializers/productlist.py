from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from djangoecommerce_app.models import Product, ProductCategory


class CategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductListSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'
        fields = ['id',
                  'name',
                  'description',
                  'thumbnail',
                  'category'
                ]
