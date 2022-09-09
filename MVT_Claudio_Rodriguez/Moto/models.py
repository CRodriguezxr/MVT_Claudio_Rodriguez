from django.db import models

class Moto(models.Model):
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    cilindrada = models.FloatField()
    precio = models.IntegerField()
    fecha_de_creacion = models.DateField(auto_now_add=True, null=True, blank=True)
