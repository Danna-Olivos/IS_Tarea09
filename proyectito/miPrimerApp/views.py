from django.shortcuts import render
import random

# Create your views here.

def suma (request):
    a = 5
    b = 10
    resultado = a + b
    return render(request, 'suma.html', {'resultado': resultado})


def minerales (request):
    return render(request,"minerales.html")

def saludo (request):
    return render(request,"saludo.html")

def minecraft (request):
    return render(request,"minecraft.html")

def cambiar_color(request):
    opciones = [
        {"color": "#e74c3c", "nombre": "rojo"},
        {"color": "#2ecc71", "nombre": "verde"},
        {"color": "#3498db", "nombre": "azul"},
        {"color": "#f39c12", "nombre": "naranja"},
        {"color": "#9b59b6", "nombre": "morado"},
    ]

    seleccionado = random.choice(opciones)

    return render(request, "color_response.html", {
        "color": seleccionado["color"],
        "nombre": seleccionado["nombre"],
    })
