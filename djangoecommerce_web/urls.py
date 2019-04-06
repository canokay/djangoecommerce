from django.conf.urls import url

from djangoecommerce_web.views import IndexView, LoginView, RegisterView

app_name = 'djangoecommerce_web'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^register/$', RegisterView, name='register'),
]
