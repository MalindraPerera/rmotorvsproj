from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from products.forms import ProductForm
from products.models import Product


def index(request):

    products = Product.objects

    query = request.GET.get("q")

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(brand__name__icontains=query)
        )

    context = {'products': products.all}
    return render(request, 'products/index.html', context)


def detail(request, product_id):
    products = Product.objects.all()
    product_id = int(product_id)

    form = ProductForm(
        initial={
            'name': Product.objects.get(id=product_id).name,
            'quantity': Product.objects.get(id=product_id).quantity,
            'description': Product.objects.get(id=product_id).description,
            'skq': Product.objects.get(id=product_id).skq,
            'category': Product.objects.get(id=product_id).category,
            'brand': Product.objects.get(id=product_id).brand,
            'purchases': Product.objects.get(id=product_id).purchases,
            'serial': Product.objects.get(id=product_id).serial,
            'unit_cost': Product.objects.get(id=product_id).unit_cost,
            'selling_price': Product.objects.get(id=product_id).selling_price,
            'rack_location': Product.objects.get(id=product_id).rack_location,
            'notes': Product.objects.get(id=product_id).notes,
        }
    )

    form_post = ProductForm(request.POST)

    if form_post.is_valid():
        form_post.auto_id = product_id
        profile = form_post.save()
        profile.pk = product_id
        profile.save()

    context = {'products': products, 'product_id': product_id, "product_form": form}
    return render(request, 'products/product-details.html', context)


def add_product(request):
    form = ProductForm()
    form_post = ProductForm(request.POST)
    status = "none"
    return_string= 'products/add-product.html'

    if form_post.is_valid():
        status = "pass"
        profile = form_post.save(commit=False)
        profile.user = request.user
        profile.active = True
        profile.save()

    products = Product.objects.all()
    context = {'products': products, 'product_form': form, "status": status}
    return render(request, return_string, context)


def validate_model(request):
    model = request.GET.get('model', None)

    data = {
        'is_taken': Product.objects.filter(model__iexact=model).exists()
    }

    if data['is_taken']:
        data['error_message'] = 'A product with this model already exists.'
    return JsonResponse(data)


def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.active = False
    product.save()
    return HttpResponseRedirect('/products')
