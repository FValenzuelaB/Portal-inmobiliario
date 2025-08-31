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
    path("inmuebles/", InmuebleListView.as_view(), name="inmuebles"),
    path("crear_inmueble/", InmuebleCreateView.as_view(), name="crear_inmueble"),
    path("actualizar_inmueble/<int:pk>/", InmuebleUpdateView.as_view(), name="actualizar_inmueble"),
    path("borrar_inmueble/<int:pk>/", InmuebleDeleteView.as_view(), name="borrar_inmueble"),
    #===URLS DE SOLICITUDES===
    path("solicitudes/", SolicitudListView.as_view(), name="solicitudes"),
    path("crear_solicitud/", SolicitudCreateView.as_view(), name="crear_solicitud"),

]