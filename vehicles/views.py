from django.db.models import Q
from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

from vehicles.forms import VehicleForm
from vehicles.models import Vehicle


def index(request):

    all_vehicles = Vehicle.objects

    query = request.GET.get("q")

    if query:
        all_vehicles = all_vehicles.filter(
            Q(model__icontains=query) |
            Q(Brand__name__icontains=query)
            )

    context = {'all_vehicles': all_vehicles.all}

    return TemplateResponse(request, 'vehicles/index.html', context)


def detail(request, vehicle_id):

    vehicles = Vehicle.objects.all()
    vehicle_id = int(vehicle_id)

    form = VehicleForm(
        initial={
            'model': Vehicle.objects.get(id=vehicle_id).model,
            'year': Vehicle.objects.get(id=vehicle_id).year,
            'Brand': Vehicle.objects.get(id=vehicle_id).Brand,
        }
    )

    form_post = VehicleForm(request.POST)

    if form_post.is_valid():
        form_post.auto_id = vehicle_id
        profile = form_post.save()
        profile.pk = vehicle_id
        profile.save()

    context = {'vehicles': vehicles, 'vehicle_id': vehicle_id, "vehicleform": form}
    return render(request, 'vehicles/vehicle-details.html', context)


def results(request, vehicle_id):
    return HttpResponse("Results of the vehicle %s" % vehicle_id)


def addVehicle(request):
    form = VehicleForm()
    form_post = VehicleForm(request.POST)
    status = "none"

    if form_post.is_valid():
        status = "pass"
        profile = form_post.save(commit=False)
        profile.user = request.user
        profile.save()

    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles, 'vehicleform': form, "status" : status}
    return render(request, 'vehicles/add-vehicle.html', context)

