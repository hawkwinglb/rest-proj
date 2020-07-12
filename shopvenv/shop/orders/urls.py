from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = "orders"
urlpatterns = [url(r'^create/$', views.order_create, name='order_create'),
               url(r'^order_list/$', views.order_list, name='order_list'),
               url(r'^(?P<id>\d+)/(?P<created>[-\w]+)/$', views.order_detail, name="order_detail"),
               ]