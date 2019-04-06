from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from djangoecommerce_app.models import Product


class FeedSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name'
        ]
