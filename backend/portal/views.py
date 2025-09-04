from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .form import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect
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
    PerfilUser,
)
from .form import (
    RegionForm,
    ComunaForm,
    InmuebleForm,
    SolicitudForm,
    PerfilUserForm,
)

#def home(request):
    #inmuebles = Inmueble.objects.all()  # Trae todos los inmuebles de la base de datos
    #return render(request, "web/home.html", {"inmuebles": inmuebles})


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
    template_name = "web/home.html"
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
    success_url = reverse_lazy("perfil")  # o donde quieras

    def dispatch(self, request, *args, **kwargs):
        # Cargamos el inmueble una vez para reutilizarlo
        self.inmueble = get_object_or_404(Inmueble, pk=kwargs["inmueble_pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["inmueble"] = self.inmueble
        return ctx

    def form_valid(self, form):
        solicitud = form.save(commit=False)
        solicitud.inmueble = self.inmueble
        solicitud.arrendatario = self.request.user
        solicitud.save()
        messages.success(self.request, "¡Solicitud enviada con éxito!")
        return redirect(self.success_url)

class SolicitudUpdateView(UpdateView):
    model = SolicitudArriendo
    form_class = SolicitudForm
    template_name = "inmuebles/solicitud_form.html"
    success_url = reverse_lazy("solicitudes")

class SolicitudeDeleteView(DeleteView):
    model = SolicitudArriendo
    template_name = 'inmuebles/borrar_solicitud.html'
    success_url = reverse_lazy('solicitudes')
#====================================================

# ===CRUD PARA USER===
#class PerfilUserListView(ListView):
    #model = PerfilUser
    #template_name = "inmuebles/perfiles_list.html"
    #context_object_name = "perfiles"

class PerfilUserCreateView(CreateView):
    model = PerfilUser
    form_class = PerfilUserForm
    template_name = "usuarios/perfil_form.html"
    success_url = reverse_lazy("solicitudes")

class PerfilUserUpdateView(UpdateView):
    model = PerfilUser
    form_class = PerfilUserForm
    template_name = "usuarios/perfil_form.html"
    success_url = reverse_lazy("solicitudes")



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)  # 👈 IMPORTANTE
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("inmuebles")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Has iniciado sesión.")
        return redirect("inmuebles")
    return render(request, "registration/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect("login")