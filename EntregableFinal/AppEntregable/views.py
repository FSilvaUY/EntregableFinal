from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppEntregable.forms import *
from AppEntregable.models import *
# Create your views here.

def inicio(self):
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def textos(self):
    plantilla = loader.get_template("textos-menu.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def hanselYGretel(self):
    plantilla = loader.get_template("hansel-gretel.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def gatoConBotas(self):
    plantilla = loader.get_template("gato-con-botas.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def tresCerditos(self):
    plantilla = loader.get_template("tres-cerditos.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def crear_libro(request):
    if request.method == "POST":
        miFormulario = Libro_form(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre= informacion["nombre"]
            autor= informacion["autor"]
            descripcion= informacion["descripcion"]
            libro = Libro (nombre=nombre, autor=autor, descripcion=descripcion)
            libro.save()
            return render(request, "crear_libro.html")

    else:
        miFormulario = Libro_form()
    
    return render(request, "crear_libro.html", {"miFormulario":miFormulario})

def busqueda_libro(request):
    return render(request, "busqueda_libro.html")

def buscar_libro(request):
    if request.GET.get("nombre", False):
        nombre = request.GET["nombre"]
        autor = Libro.objects.filter(nombre = nombre)

        return render(request, "resultado_de_libro.html", {"autor":autor})
    else:
        respuesta = "No se encontro ningun libro"
    return HttpResponse(respuesta)