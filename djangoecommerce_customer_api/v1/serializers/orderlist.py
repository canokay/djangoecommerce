from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from djangoecommerce_app.models import Order


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id',
                  'card',
                  'transaction_id',
                  'transaction_time',
                  'transaction_total_amount',
                  'status',
                ]
