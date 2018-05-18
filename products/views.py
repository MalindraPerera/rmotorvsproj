# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product


def index(request):
    latest_products = Product.objects.order_by('-Name')[:5]
    context = {'latest_products': latest_products}
    return render(request, 'products/index.html', context)


def detail(request, product_id):
    products = Product.objects.all()
    product_id = int(product_id)
    context = {'products': products, 'product_id': product_id}
    return render(request, 'products/product-details.html', context)


def results(request, product_id):
    return HttpResponse("Results of the products %s" % product_id)


def addProduct(request, product_id):
    return HttpResponse("Add product details %s" % product_id)