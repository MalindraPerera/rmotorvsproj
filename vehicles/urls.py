from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<vehicle_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^add-vehicle$', views.add_vehicle, name="add_vehicle"),
    url(r'^(?P<vehicle_id>[0-9]+)/delete$', views.vehicle_delete, name='delete_vehicle'),
    url(r'^(?P<vehicle_id>[0-9]+)/vehicle-details$', views.vehicle_update, name='update_vehicle'),
    url(r'^ajax/validate_model/$', views.validate_model, name='validate_model'),
]