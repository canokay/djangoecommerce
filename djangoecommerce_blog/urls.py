from django.conf.urls import url
from djangoecommerce_blog.views import IndexView,BlogListView,CategoryListView,BlogDetailView,HashtagListView


app_name = 'djangoecommerce_blog'


urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^blog/$', BlogListView, name='blog_all'),
    url(r'^blog/(?P<slug>[-\w]+)/$',BlogDetailView, name='blog_single'),
    url(r'^category/(?P<category_slug>[-\w]+)/$',CategoryListView, name='category_all'),
    url(r'^hashtag/(?P<hashtag>[-\w]+)/$',HashtagListView, name='hashtag'),
]
