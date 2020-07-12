from django.conf.urls import url
from django.views.generic import ListView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

from .views import SearchProductsView



app_name = "foodshop"
urlpatterns = [
    url(r'^index/$', views.product_list, name='product_list'),
    url(r"^search/$", SearchProductsView.as_view(), name="search_view"),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()