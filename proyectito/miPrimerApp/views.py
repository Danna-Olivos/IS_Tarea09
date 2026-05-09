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
    
#para hx-vals 
def fabricar_item(request):

    if request.method == 'GET':
        try:
            material1 = request.GET.get('material1', 'ninguno')
            material2 = request.GET.get('material2', 'ninguno')
            cantidad = int(request.GET.get('cantidad', 1))
            
            # Recetas
            recetas = {
                ('palo', 'carbon'): 'Antorcha',
                ('diamante', 'palo'): 'Pico de Diamante',
                ('madera', 'madera'): 'Tablones de Madera',
            }
            
            # Buscar receta
            receta_clave = (material1, material2) if (material1, material2) in recetas else (material2, material1)
            item_fabricado = recetas.get(receta_clave, 'Receta inválida')
            
            if item_fabricado != 'Receta inválida':
                return HttpResponse(f'''
                    <div style="margin-top: 15px; padding: 15px; background: #2d5016; border-radius: 8px; border-left: 4px solid #ffaa00; color: white;">
                        <strong>Crafteo completado</strong><br>
                        Materiales usados: {cantidad}x {material1} + {cantidad}x {material2}<br>
                        Has obtenido: {item_fabricado} x{cantidad}<br>
                    </div>
                ''')
            else:
                return HttpResponse(f'''
                    <div style="margin-top: 15px; padding: 15px; background: #8b4513; border-radius: 8px; border-left: 4px solid #ff4444; color: white;">
                        <strong>Crafteo no completado</strong><br>
                        {material1} + {material2} no combinan en la mesa de crafteo.<br>
                        Prueba con: palo+carbon, diamante+palo, madera+madera
                    </div>
                ''')
        except (ValueError, TypeError):
            return HttpResponse('<div style="color: red;">Error en la mesa de crafteo</div>')

#para hx-include
def vender_minerales(request):

    if request.method == 'POST':
        # Precios de los minerales (esmeraldas que paga el aldeano)
        tabla_precios = {
            'carbon': 2,
            'hierro': 5,
            'oro': 8,
            'diamante': 15,
            'esmeralda': 20,
            'redstone': 3,
            'lapizlazuli': 4,
        }

        minerales_vendidos = []
        total_esmeraldas = 0
        
        for mineral, precio in tabla_precios.items():
            cantidad = request.POST.get(f'mineral_{mineral}', '0')
            if cantidad and int(cantidad) > 0:
                cantidad_int = int(cantidad)
                ganancia = cantidad_int * precio
                total_esmeraldas += ganancia
                minerales_vendidos.append(f"{cantidad_int}x {mineral} → {ganancia} esmeraldas")
        
        aldeano = request.POST.get('aldeano', 'Aldeano Genérico')
        
        if minerales_vendidos:
            return HttpResponse(f'''
                <div style="margin-top: 15px; padding: 15px; background: #1a472a; border-radius: 8px; border-left: 4px solid #50c878; color: white;">
                    <strong>Venta exitosa</strong><br>
                    Aldeano: {aldeano}<br>
                    Minerales vendidos:<br>
                    {''.join([f'&nbsp;&nbsp;&nbsp;• {v}<br>' for v in minerales_vendidos])}
                    <hr style="border-color: #50c878;">
                    <strong>Esmeraldas obtenidas: {total_esmeraldas} Esmeraldas</strong><br>
                </div>
            ''')
        else:
            return HttpResponse(f'''
                <div style="margin-top: 15px; padding: 15px; background: #5c3a21; border-radius: 8px; border-left: 4px solid #ffaa44; color: white;">
                    <strong>Aldeano {aldeano}:</strong><br>
                    "No tienes nada para vender:(."<br>
                </div>
            ''')
    
    return HttpResponse('<div style="color: red;">Error en la transacción</div>')