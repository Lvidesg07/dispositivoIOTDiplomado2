from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class UsuarioRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'rol')


class TarjetaRFID(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    uid = models.CharField(max_length=50, unique=True)
    estado = models.BooleanField(default=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uid