import datetime
import uuid
from urllib.parse import quote

from django.contrib.auth.models import update_last_login
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoecommerce import settings
from djangoecommerce_app.models import User, City, CompanyAddress, CompanyFeature,Card,Order, Company, ProductCategory,  Product, ProductImage, ProductBrand

from djangoecommerce_app.serializers.productlist import ProductListSerializer
from djangoecommerce_app.serializers.productdetail import ProductDetailSerializer
from djangoecommerce_app.serializers.cardlist import CardListSerializer
from djangoecommerce_app.serializers.orderlist import OrderListSerializer
from djangoecommerce_app.serializers.carddetail import CardDetailSerializer
from djangoecommerce_app.serializers.orderdetail import OrderDetailSerializer



class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        type = self.request.GET.get('type', None)
        return Product.objects.all()



class ProductDetailView(ListAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(id=id)


class CardListView(ListAPIView):
    serializer_class = CardListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        id = self.request.user.id
        return Card.objects.filter(owner=id)



class CardDetailView(ListAPIView):
    serializer_class = CardDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        id = self.kwargs['id']
        return Card.objects.filter(id=id)


class OrderListView(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        id = self.request.user.id
        return Order.objects.filter(buyer=id)


class OrderDetailView(ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        id = self.kwargs['id']
        return Order.objects.filter(id=id)
