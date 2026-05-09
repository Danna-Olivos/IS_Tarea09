from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'miPrimerApp'

urlpatterns = [
    path('suma/', views.suma, name='suma'),
    path('minerales/', views.minerales, name='minerales'),
    path('saludo/', views.saludo, name='saludo'),
    path('minecraft/', views.minecraft, name='minecraft'),
    path('cambiar-color/', views.cambiar_color, name='cambiar_color'),
    path('cambiar-imagen/', views.cambiar_imagen, name='cambiar_imagen'),
]       