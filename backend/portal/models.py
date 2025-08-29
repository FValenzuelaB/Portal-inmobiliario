from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    nro_region = models.CharField(max_length=5) #XVIII
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"Region: {self.nombre} ({self.nro_region})" #Region: Bio Bio (VIII)

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comunas") #PK de region

    def __str__(self):
        return f"Comuna {self.nombre}, Perteneciente a la región ({self.region})" # Comuna: Concepción, perteneciente a la región: Bio Bio


class Inmueble(models.Model):
    class Tipo_de_inmueble(models.TextChoices):
        casa = "CASA", _("Casa")
        departamento = "DEPARTAMENTO", _("Departamento")
        oficina = "OFICINA", _("Oficina")


    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inmuebles")
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField()
    m2_construidos = models.FloatField(default=0)
    m2_totales = models.FloatField(default=0)
    estacionamientos = models.PositiveSmallIntegerField(default=0)
    habitaciones = models.PositiveSmallIntegerField(default=0)
    banos = models.PositiveSmallIntegerField(default=0)
    direccion = models.CharField(max_length=100)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, related_name="inmuebles") #PK de Comuna
    tipo_de_inmueble = models.CharField(max_length=20, choices=Tipo_de_inmueble.choices)

    def __str__(self):
        return f"{self.tipo_de_inmueble}: {self.nombre}, Propietario: {self.propietario}"
    
class SolicitudArriendo(models.Model):
    class EstadoSolicitud(models.TextChoices):
        pendiente = "P", _("Pendiente")
        aceptada = "A", _("Aceptada")
        rechazada = "R", _("Rechazada")

    arrendatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solicitudes")
    estado = models.CharField(max_length=20, choices=EstadoSolicitud.choices, default=EstadoSolicitud.pendiente)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)