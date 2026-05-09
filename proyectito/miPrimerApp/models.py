from django.db import models

# Create your models here.
class Vaquero(models.Model):
    altura = models.IntegerField()
    recompensa = models.FloatField(default=0.0)
    es_buscado = models.BooleanField(default=False)
