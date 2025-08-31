from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import (
    Region,
    Comuna,
    Inmueble,
    SolicitudArriendo,
)
from .form import (
    RegionForm,
    ComunaForm,
    InmuebleForm,
    SolicitudForm,
)

# ===CRUD PARA REGION===

class RegionListView(ListView):
    model = Region
    template_name = "inmuebles/regiones_list.html"
    context_object_name = "regiones"

class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = "inmuebles/region_form.html"
    success_url = reverse_lazy("regiones")

class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = "inmuebles/region_form.html"
    success_url = reverse_lazy("regiones")

class RegionDeleteView(DeleteView):
    model = Region
    template_name = 'inmuebles/borrar_region.html'
    success_url = reverse_lazy('regiones')
#====================================================

# ===CRUD PARA COMUNA===

class ComunaListView(ListView):
    model = Comuna
    template_name = "inmuebles/comunas_list.html"
    context_object_name = "comunas"

class ComunaCreateView(CreateView):
    model = Comuna
    form_class = ComunaForm
    template_name = "inmuebles/comuna_form.html"
    success_url = reverse_lazy("comunas")

class ComunaUpdateView(UpdateView):
    model = Comuna
    form_class = ComunaForm
    template_name = "inmuebles/comuna_form.html"
    success_url = reverse_lazy("comunas")

class ComunaDeleteView(DeleteView):
    model = Comuna
    template_name = 'inmuebles/borrar_comuna.html'
    success_url = reverse_lazy('comunas')
#====================================================

# ===CRUD PARA INMUEBLE===

class InmuebleListView(ListView):
    model = Inmueble
    template_name = "inmuebles/inmuebles_list.html"
    context_object_name = "inmuebles"

class InmuebleCreateView(CreateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = "inmuebles/inmueble_form.html"
    success_url = reverse_lazy("inmuebles")

class InmuebleUpdateView(UpdateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = "inmuebles/inmueble_form.html"
    success_url = reverse_lazy("inmuebles")

class InmuebleDeleteView(DeleteView):
    model = Inmueble
    template_name = 'inmuebles/borrar_inmueble.html'
    success_url = reverse_lazy('inmuebles')
#====================================================

# ===CRUD PARA SOLICITUD===
class SolicitudListView(ListView):
    model = SolicitudArriendo
    template_name = "inmuebles/solicitudes_list.html"
    context_object_name = "solicitudes"

class SolicitudCreateView(CreateView):
    model = SolicitudArriendo
    form_class = SolicitudForm
    template_name = "inmuebles/solicitud_form.html"
    success_url = reverse_lazy("solicitudes")