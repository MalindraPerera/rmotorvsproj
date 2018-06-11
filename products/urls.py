from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<product_id>[0-9]+)/delete$', views.product_delete, name='delete_product'),
    url(r'^add-product$', views.add_product, name="add_product")
]