# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from concesionario.apps.ventas.forms import *
from concesionario.apps.ventas.models import *
from django.http import HttpResponseRedirect

def add_vehiculo_view(request):
	if request.method == "POST":
		formulario = add_vehiculo_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.estado = "Disponible"
			add.save()
			return HttpResponseRedirect('/vehiculo/%s' %add.id)
	else:
		formulario = add_vehiculo_form()
	ctx = {'form':formulario}
	return render_to_response('ventas/add_vehiculo.html', ctx, context_instance = RequestContext(request))