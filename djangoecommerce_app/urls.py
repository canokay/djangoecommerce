from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include
from rest_framework import routers

from FindBikeFriends import settings
from djangoecommerce_app.api import FeedView, ProductDetailView

app_name = 'djangoecommerce_app'
router = routers.DefaultRouter()

urlpatterns = \
    [
        url(r'^', include(router.urls)),
        url(r'^event/$', FeedView.as_view()),
        url(r'^event/(?P<id>\d+)/$', ProductDetailView.as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
