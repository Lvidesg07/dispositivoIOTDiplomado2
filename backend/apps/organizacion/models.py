from django.db import models

class Organizacion(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Sede(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Zona(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    nivel_seguridad = models.IntegerField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class PuertaAcceso(models.Model):
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre