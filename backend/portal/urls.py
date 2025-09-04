from django.urls import path
from .views import *

urlpatterns = [
    path("regiones/", RegionListView.as_view(), name="regiones"),
    path("crear_region/", RegionCreateView.as_view(), name="crear_region"),
    path("actualizar_region/<int:pk>/", RegionUpdateView.as_view(), name="actualizar_region"),
    path("borrar_region/<int:pk>/", RegionDeleteView.as_view(), name="borrar_region"),
    #===URLS DE COMUNAS===
    path("comunas/", ComunaListView.as_view(), name="comunas"),
    path("crear_comuna/", ComunaCreateView.as_view(), name="crear_comuna"),
    path("actualizar_comuna/<int:pk>/", ComunaUpdateView.as_view(), name="actualizar_comuna"),
    path("borrar_comuna/<int:pk>/", ComunaDeleteView.as_view(), name="borrar_comuna"),
    #===URLS DE INMUEBLES===
    path("", InmuebleListView.as_view(), name="inmuebles"),
    path("crear_inmueble/", InmuebleCreateView.as_view(), name="crear_inmueble"),
    path("actualizar_inmueble/<int:pk>/", InmuebleUpdateView.as_view(), name="actualizar_inmueble"),
    path("borrar_inmueble/<int:pk>/", InmuebleDeleteView.as_view(), name="borrar_inmueble"),
    #===URLS DE SOLICITUDES===
    path("solicitudes/", SolicitudListView.as_view(), name="solicitudes"),
    path("crear_solicitud/", SolicitudCreateView.as_view(), name="crear_solicitud"),
    path("actualizar_solicitud/<int:pk>/", SolicitudUpdateView.as_view(), name="actualizar_solicitud"),
    path("borrar_solicitud/<int:pk>/", SolicitudeDeleteView.as_view(), name="borrar_solicitud"),
    path("solicitudes/nueva/<int:inmueble_pk>/",SolicitudCreateView.as_view(), name="solicitud_create_for_inmueble"),
    #===URLS DE PERFIL===
    path("crear_perfil/", PerfilUserCreateView.as_view(), name="crear_perfil"),
    path("actualizar_perfil/<int:pk>/", PerfilUserUpdateView.as_view(), name="actualizar_perfil"),
    #===GENERALES===
    #path("", home , name="home"),
    path("accounts/login/",  login_view,  name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    path("accounts/register/", register_view, name="register"),
]