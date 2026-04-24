from django.contrib import admin
from .models import Organizacion, Sede, Zona, PuertaAcceso

admin.site.register(Organizacion)
admin.site.register(Sede)
admin.site.register(Zona)
admin.site.register(PuertaAcceso)