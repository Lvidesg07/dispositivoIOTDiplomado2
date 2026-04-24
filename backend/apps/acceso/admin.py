from django.contrib import admin
from .models import PermisoAcceso, IntentoAcceso, EstadoPuerta

admin.site.register(PermisoAcceso)
admin.site.register(IntentoAcceso)
admin.site.register(EstadoPuerta)