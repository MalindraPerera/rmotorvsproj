from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator

from vehicles.forms import VehicleForm
from vehicles.models import Vehicle


def index(request):
    vehicles = Vehicle.objects

    query = request.GET.get("q")

    if query:
        vehicles = vehicles.filter(
            Q(model__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(year__year__icontains=query)
        )

    context = {'vehicles': vehicles.all}

    return render(request, 'vehicles/index.html', context)


def detail(request, vehicle_id):
    vehicles = Vehicle.objects.all()
    vehicle_id = int(vehicle_id)

    form = VehicleForm(
        initial={
            'model': Vehicle.objects.get(id=vehicle_id).model,
            'year': Vehicle.objects.get(id=vehicle_id).year,
            'brand': Vehicle.objects.get(id=vehicle_id).brand
        }
    )

    if request.method == 'POST':
        form_post = VehicleForm(request.POST)

    #Temporary fix which deletes the extra vehicles created when adding
        if form_post.is_valid():
            form_post.auto_id = Vehicle.objects.get(id=vehicle_id).id
            profile = form_post.save()
            profile.pk = form_post.auto_id
            profile.save()

            vehicle = Vehicle.objects.get(id=vehicle_id+1)
            vehicle.active = False
            vehicle.save()

    context = {'vehicles': vehicles, 'vehicle_id': vehicle_id, "vehicle_form": form}
    return render(request, 'vehicles/vehicle-details.html', context)


def add_vehicle(request):
    form = VehicleForm()
    form_post = VehicleForm(request.POST)
    status = "none"
    return_string = 'vehicles/add-vehicle.html'

    if form_post.is_valid():
        status = "pass"
        profile = form_post.save(commit=False)
        profile.user = request.user
        profile.active = True
        profile.save()

    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles, 'vehicle_form': form, "status": status}
    return render(request, return_string, context)


def validate_model(request):
    model = request.GET.get('model', None)

    data = {
        'is_taken': Vehicle.objects.filter(model__iexact=model).exists()
    }

    if data['is_taken']:
        data['error_message'] = 'A vehicle with this model already exists.'
    return JsonResponse(data)


def vehicle_delete(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    vehicle.active = False
    vehicle.save()
    return HttpResponseRedirect('/vehicles')


def vehicle_update(request, vehicle_id):
    instance = Vehicle.objects.get(id=vehicle_id)
    form = VehicleForm(request.POST or None, instance=instance)

    vehicles = Vehicle.objects.all

    if form.is_valid():
        form.save()
        return HttpResponse('/vehicles')

        return render(request, 'index.html', {'form': form})