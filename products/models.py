from django.db import models


# Create your models here.
class Product(models.Model):
    skq = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('ProductBrand', on_delete=models.CASCADE)
    purchases = models.ForeignKey('ProductPurchase', on_delete=models.CASCADE)
    serial = models.CharField(max_length=250)
    quantity = models.FloatField()
    unit_cost = models.FloatField()
    selling_price = models.FloatField()
    rack_location = models.FloatField()
    notes = models.CharField(max_length=250)
    product_is_spare = models.BooleanField
    description = models.CharField(max_length=250)
    #hidden boolean
    active = models.BooleanField();


    def __str__(self):
        return self.name


class ProductPurchase(models.Model):
    description = models.CharField(max_length=250)
    status = models.IntegerField(1)

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ProductBrand(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name