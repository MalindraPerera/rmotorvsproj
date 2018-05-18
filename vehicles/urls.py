from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<vehicle_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<vehicle_id>[0-9]+)/results$', views.results, name="results"),
    url(r'^add-vehicle$', views.addVehicle, name="addVehicle")
]