from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from djangoecommerce_app.models import Card

class CardDetailSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ['id',
                  'owner',
                  'product',
                  'status',
                  'transaction_time',
                  'transaction_total_amount',
                 ]
