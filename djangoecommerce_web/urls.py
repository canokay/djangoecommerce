from django.conf.urls import url

from djangoecommerce_web.views import IndexView, ProductDetailView, BlogDetailView

app_name = 'djangoecommerce_web'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^urun/(?P<id>[-\w]+)/$',ProductDetailView, name='product_detail'),
]
