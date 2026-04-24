from django.contrib import admin
from .models import Usuario, Rol, UsuarioRol, TarjetaRFID

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(UsuarioRol)
admin.site.register(TarjetaRFID)