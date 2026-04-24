from django.db import models
from apps.usuarios.models import Usuario

class AuditoriaSistema(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
    accion = models.CharField(max_length=100)
    tabla_afectada = models.CharField(max_length=50)
    registro_id = models.IntegerField()
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()