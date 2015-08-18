from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# MaxValueValidator sirve para definir el valor maximo de un campo numerico se hace con validator[MaxValueValidator(maximo valor)]

# Create your models here. 
class Categoria(models.Model):
	nombre				= models.CharField(max_length = 20, unique = True)
	descripcion 		= models.TextField(max_length = 500)

	def __unicode__ (self):
		return self.nombre

class Carriceria(models.Model):
	nombre				= models.CharField(max_length = 20)

class Automovil(models.Model):
	estados = (
			(u'disponible',u'Dispoible'),
			(u'no_dispobile',u'No disponible'),
		)
	combustible = (
			(u'gasolina',u'Gasolina'),
			(u'acpm',u'ACPM'),
			(u'electrico',u'Electrico'),
		)
	nombre 				= models.CharField(max_length = 20)
	marca				= models.CharField(max_length = 10, default = "Ferrari")
	modelo				= models.CharField(max_length = 20)	
	anio				= models.IntegerField(validators=[MaxValueValidator(2016)])
	color				= models.CharField(max_length = 20)
	numero_puertas		= models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(2)])
	capacidad_pasajeros = models.IntegerField(validators =[MaxValueValidator(9), MinValueValidator(1)])
	tipo_carroceria		= models.ForeignKey(Carriceria)
	Categoria			= models.ForeignKey(Categoria)
	tipo_combustible	= models.CharField(max_length = 10, choices = combustible, default ="Gasolina")
	descripcion 		= models.TextField(max_length = 500)
	numero_motor		= models.CharField(max_length = 10)
	numero_chasis		= models.CharField(max_length = 10)
	precio				= models.DecimalField(max_digits = 10, decimal_places = 5)
	estado				= models.CharField(max_length = 10, choices = estados, default = "Dispoible")
	fecha 				= models.DateField(auto_now_add = True)
	def __unicode__(self):
		return self.nombre

#class Cliente(models.Model):
#	identificacion		= models.CharField(max_length = 15, unique = True)
#	nombre 				= models.CharField(max_length = 30)
#	primer_apellido		= models.CharField(max_length = 20)
#	seugndo_apellido	= models.CharField(max_length = 20)--->