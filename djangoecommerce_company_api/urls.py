from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include
from rest_framework import routers

from djangoecommerce import settings

app_name = 'djangoecommerce_company_api'
router = routers.DefaultRouter()

urlpatterns = \
    [
        url(r'^v1/', include('djangoecommerce_company_api.v1.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)