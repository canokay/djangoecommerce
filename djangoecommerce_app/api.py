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
from djangoecommerce_app.models import User, City, CompanyAddress, CompanyFeature, Company, ProductCategory,  Product, ProductImage, ProductBrand

from djangoecommerce_app.serializers.productlist import ProductListSerializer
from djangoecommerce_app.serializers.productdetail import ProductDetailSerializer




class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        type = self.request.GET.get('type', None)
        return Product.objects.all()



class ProductDetailView(ListAPIView):
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(id=id)
