from django.db import models

# Create your models here.

class Reservas(models.Model):
    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=50)
    fechayHoraDeReserva = models.DateTimeField()
    cantidadDePersonas = models.IntegerField()
    correo = models.EmailField()
    estado = models.CharField(max_length=30)
    observaciones = models.TextField(blank=True, null=True)
