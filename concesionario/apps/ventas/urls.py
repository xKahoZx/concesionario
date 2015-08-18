from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('concesionario.apps.ventas.views',

		url(r'^add/vehiculo/$','add_vehiculo_view', name = 'vista_agregar_vehiculo'),

	)