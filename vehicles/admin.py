from django.contrib import admin

# Register your models here.
from vehicles.models import Vehicle, VehicleBrand

admin.site.register(Vehicle)
admin.site.register(VehicleBrand)