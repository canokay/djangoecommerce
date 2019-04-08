from django.conf.urls import url

from djangoecommerce_web.views import IndexView

app_name = 'djangoecommerce_web'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
]
