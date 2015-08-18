from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# MaxValueValidator sirve para definir el valor maximo de un campo numerico se hace con validator[MaxValueValidator(maximo valor)]

# Create your models here. 
class Categoria(models.Model):
	nombre				= models.CharField(max_length = 20, unique = True)
	descripcion 		= models.TextField(max_length = 500)

	def __unicode__ (self):
		return self.nombre

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
	carroceria = (
			(u'Berlinetta',u'Berlinetta'),
			(u'Cupe',u'Cupe'),
			(u'Capota_rigida',u'Capota rigida'),
			(u'Cabriolet',u'Cabriolet'),
			(u'Familiar',u'Familiar'),
			(u'Fastback',u'Fastback'),
			(u'Furgoneta',u'Furgoneta'),
			(u'Hardtop',u'Hardtop'),
			(u'Hatchback',u'Hatchback'),
			(u'Kammback',u'Kammback'),
			(u'Liftback',u'Liftback'),
			(u'Limusina',u'Limusina'),
			(u'Monovolumen',u'Monovolumen'),
			(u'Notchback',u'Notchback'),
			(u'Pick_Up',u'Pick Up'),
			(u'Sedan',u'Sedan'),
			(u'Tricuerpo',u'Tricuerpo'),
			(u'Todoterreno',u'Todoterreno'),
		)
	nombre 				= models.CharField(max_length = 20)
	marca				= models.CharField(max_length = 10, default = "Ferrari")
	modelo				= models.CharField(max_length = 20)	
	anio				= models.IntegerField(validators=[MaxValueValidator(2016)])
	color				= models.CharField(max_length = 20)
	numero_puertas		= models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(2)])
	capacidad_pasajeros = models.IntegerField(validators =[MaxValueValidator(9), MinValueValidator(1)])
	tipo_carroceria		= models.CharField(max_length = 20 , choices = carroceria, default = "Berlinetta")
	Categoria			= models.ForeignKey(Categoria)
	tipo_combustible	= models.CharField(max_length = 10, choices = combustible, default ="Gasolina")
	cilindraje			= models.CharField(max_length = 6)
	numero_motor		= models.CharField(max_length = 10)
	numero_chasis		= models.CharField(max_length = 10)
	precio				= models.DecimalField(max_digits = 10, decimal_places = 5)
	estado				= models.CharField(max_length = 10, choices = estados, default = "Dispoible")
	fecha 				= models.DateField(auto_now_add = True)
	def __unicode__(self):
		return self.nombre

class Cliente(models.Model):
	identificacion		= models.IntegerField(primary_key = True)
	nombre				= models.CharField(max_length = 30)
	primer_apellido		= models.CharField(max_length = 20)
	segundo_apellido	= models.CharField(max_length = 20)
	correo				= models.EmailField()
	telefono			= models.CharField(max_length = 15)

	def __unicode__(self):
		return self.nombre

class Vendedor(models.Model):
	estado = (
		(u'activo',u'Activo'),
		(u'inactivo',u'Incativo'),
		)
	identificacion		= models.IntegerField(primary_key = True)
	nombre				= models.CharField(max_length = 30)
	primer_apellido		= models.CharField(max_length = 20)
	segundo_apellido	= models.CharField(max_length = 20)
	correo				= models.EmailField()
	telefono			= models.CharField(max_length = 15)
	estatus				= models.CharField(max_length = 10, choices = estado)
	numero_seguro		= models.CharField(max_length = 20)

	def __unicode__(self):
		return self.nombre


class Venta(models.Model):
	automovil 			= models.ForeignKey(Automovil)
	vendedor			= models.ForeignKey(Vendedor)
	cliente 			= models.ForeignKey(Cliente)
	total_venta			= models.DecimalField(max_digits = 10, decimal_places = 5)
	fecha_venta			= models.DateField(auto_now_add = True)

	def __unicode__(self):
		return self.vendedor.nombre