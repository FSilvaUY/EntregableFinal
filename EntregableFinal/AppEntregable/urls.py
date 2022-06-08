from django.urls import path
from AppEntregable import views
from AppEntregable.views import *
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("textos/", textos, name="textos"),
    path("textos/hansel-gretel.html", hanselYGretel, name="hansel_gretel"),
    path("textos/gato-con-botas.html", gatoConBotas, name="gato_con_botas"),
    path("textos/tres-cerditos.html/", tresCerditos, name="tres_cerditos"),
    path("textos/crear_libro/", crear_libro, name="crear_libro"),
    path("textos/busqueda_libro/", busqueda_libro, name="busqueda_libro"),
    path("textos/buscar_libro/", buscar_libro, name="buscar_libro"),
] 