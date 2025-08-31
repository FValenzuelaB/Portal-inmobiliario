from django import forms
from .models import *



class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nro_region', 'nombre']

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['region', 'nombre']

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['propietario', 'nombre', 'descripcion',
                   'm2_construidos', 'm2_totales', 'estacionamientos',
                     'habitaciones', 'banos', 'direccion', 
                     'precio_mensual', 'comuna', 'tipo_de_inmueble']
        
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['inmueble', 'arrendatario', 'mensaje', 'estado']
