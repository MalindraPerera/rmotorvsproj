from django.contrib import admin

# Register your models here.
from products.models import Product, ProductPurchases, Categories, ProductBrands

admin.site.register(Product)
admin.site.register(ProductPurchases)
admin.site.register(Categories)
admin.site.register(ProductBrands)