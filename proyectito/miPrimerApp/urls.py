from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'miPrimerApp'

urlpatterns = [
    path('suma/', views.suma, name='suma'),
    path('minerales/', views.minerales, name='minerales'),
    path('saludo/', views.saludo, name='saludo'),
    path('minecraft/', views.minecraft, name='minecraft'),
]       