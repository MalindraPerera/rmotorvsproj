from django.db import models


class Vehicle(models.Model):
    model = models.CharField(max_length=250)
    year = models.DateField()
    Brand = models.ForeignKey('VehicleBrand', on_delete=models.CASCADE)

    def __str__(self):
        return self.model


class VehicleBrand(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
