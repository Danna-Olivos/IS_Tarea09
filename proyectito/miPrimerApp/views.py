from django.shortcuts import render
import random
import time
from django.http import HttpResponse

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

def cambiar_imagen(request):
    # Simulamos retraso para ver el spinner (hx-indicator)
    time.sleep(1) 
    
    # Miramos qué imagen tiene el usuario actualmente
    actual = request.GET.get('img', 'original')
    
    if actual == 'original':
        # Si tiene la original, mandamos la alternativa y cambiamos el parámetro del botón
        return HttpResponse('''
            <img id="imagen-minecraft" src="/static/OtraImagenMinecraft.png" width="500">
            <script>
                // Actualizamos el botón para que la próxima vez pida la original
                document.querySelector('[hx-get*="/cambiar-imagen/"]').setAttribute("hx-get", "/cambiar-imagen/?img=otra");
                htmx.process(document.body); // Refrescamos HTMX para que reconozca el cambio
            </script>
        ''')
    else:
        # Si tiene la otra, mandamos la original
        return HttpResponse('''
            <img id="imagen-minecraft" src="/static/MineralesMinecraft.jpg" width="500">
            <script>
                document.querySelector('[hx-get*="/cambiar-imagen/"]').setAttribute("hx-get", "/cambiar-imagen/?img=original");
                htmx.process(document.body);
            </script>
        ''')