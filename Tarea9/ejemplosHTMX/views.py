from django.shortcuts import render
from django.http import HttpResponse

def vista_suma(request):
    # Esta renderiza la página principal de tu ejemplo
    return render(request, 'suma.html')

def registrar_clic_silencioso(request):
    # Esta función se ejecuta en el servidor, pero no envía HTML de vuelta
    print(">>> [SERVIDOR]: Se recibió una petición silenciosa (hx-swap='none')")
    return HttpResponse("")