from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^',  include("djangoecommerce_web.urls")),
    url(r'^musteri/', include("djangoecommerce_customer.urls")),
    url(r'^sirket/', include("djangoecommerce_company.urls")),
]
