from django import forms
from vehicles.models import Vehicle


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        exclude = ['active',]