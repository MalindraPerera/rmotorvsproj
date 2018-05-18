from django.db import models


# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=250)
    Price = models.FloatField()
    Quantity = models.FloatField()
    Description = models.CharField(max_length=250)
    Brand = models.CharField(max_length=250)
    skq = models.CharField(max_length=250)
    Category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    Brand = models.ForeignKey('ProductBrands', on_delete=models.CASCADE)
    Purchases = models.ForeignKey('ProductPurchases', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class ProductPurchases(models.Model):
    description = models.CharField(max_length=250)
    status = models.IntegerField(1)

    def __str__(self):
        return self.description


class Categories(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ProductBrands(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name