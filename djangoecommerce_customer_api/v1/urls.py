from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include
from rest_framework import routers

from djangoecommerce import settings
from djangoecommerce_customer_api.v1.api import ProductListView, ProductDetailView,CardListView,OrderListView, CardDetailView, OrderDetailView


app_name = 'djangoecommerce_customer_api'
router = routers.DefaultRouter()

urlpatterns = \
    [
        url(r'^', include(router.urls)),
        url(r'^product/$', ProductListView.as_view()),
        url(r'^card/$', CardListView.as_view()),
        url(r'^order/$', OrderListView.as_view()),
        url(r'^product/(?P<id>\d+)/$', ProductDetailView.as_view()),
        url(r'^card/(?P<id>\d+)/$', CardDetailView.as_view()),
        url(r'^order/(?P<id>\d+)/$', OrderDetailView.as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
