from django.db import models
from apps.organizacion.models import PuertaAcceso

class Dispositivo(models.Model):
    puerta_acceso = models.OneToOneField(PuertaAcceso, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    mac = models.CharField(max_length=50, null=True, blank=True)
    firmware_version = models.CharField(max_length=20, null=True, blank=True)
    estado = models.BooleanField(default=True)
    ultima_conexion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.tipo


class EventoPIR(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    movimiento = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)


class ComandoRemoto(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    comando = models.CharField(max_length=50)
    parametro = models.CharField(max_length=100, null=True, blank=True)
    respuesta = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=20)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)