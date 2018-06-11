from django.contrib import admin

# Register your models here.
from products.models import Product, ProductPurchase, Category, ProductBrand

admin.site.register(Product)
admin.site.register(ProductPurchase)
admin.site.register(Category)
admin.site.register(ProductBrand)