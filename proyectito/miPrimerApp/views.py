from django.shortcuts import render

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
