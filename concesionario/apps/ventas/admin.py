from django.contrib import admin
from concesionario.apps.ventas.models import *

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Automovil)
admin.site.register(Vendedor)
admin.site.register(Venta)