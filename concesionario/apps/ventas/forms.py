from django import forms
from concesionario.apps.ventas.models import *

class add_vehiculo_form(forms.ModelForm):
	class Meta:
		model = Automovil
		exclude = {'estado', 'marca'}
