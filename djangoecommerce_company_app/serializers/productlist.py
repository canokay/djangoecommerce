from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from djangoecommerce_app.models import Product, ProductCategory


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id',
                  'category',
                ]


class ProductListSerializer(ModelSerializer):
    category = ProductCategorySerializer()
    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'description',
                  'thumbnail',
                  'category'
                ]
