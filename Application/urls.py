from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^vehicles/', include('vehicles.urls')),
    url(r'^products/', include('products.urls'))
]

