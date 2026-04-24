from django.db import models
from apps.usuarios.models import Usuario, Rol, TarjetaRFID
from apps.organizacion.models import PuertaAcceso

class PermisoAcceso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    puerta_acceso = models.ForeignKey(PuertaAcceso, on_delete=models.CASCADE)
    horario_inicio = models.TimeField(null=True, blank=True)
    horario_fin = models.TimeField(null=True, blank=True)
    dias_semana = models.CharField(max_length=20, null=True, blank=True)
    estado = models.BooleanField(default=True)


class IntentoAcceso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puerta_acceso = models.ForeignKey(PuertaAcceso, on_delete=models.CASCADE)
    tarjeta_rfid = models.ForeignKey(TarjetaRFID, null=True, blank=True, on_delete=models.SET_NULL)
    fecha = models.DateTimeField(auto_now_add=True)
    resultado = models.CharField(max_length=20)
    motivo = models.CharField(max_length=150)


class EstadoPuerta(models.Model):
    puerta_acceso = models.ForeignKey(PuertaAcceso, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)