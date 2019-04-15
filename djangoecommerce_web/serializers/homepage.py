from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from djangoecommerce_app.models import Product, ProductCategory
from djangoecommerce_blog.models import Blog

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
                  'category',
                  'price'
                ]

class BlogListSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id',
                  'title',
                  'thumbnail',
                  'slug'
                 ]

class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'description',
                  'created_at',
                  'category',
                  'owner',
                  'brand',
                  'price',
                  'thumbnail'
                 ]


class BlogDetailSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id',
                  'title',
                  'thumbnail',
                  'slug'
                 ]
