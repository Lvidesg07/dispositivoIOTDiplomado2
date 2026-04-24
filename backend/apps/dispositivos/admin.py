from django.contrib import admin
from .models import Dispositivo, EventoPIR, ComandoRemoto

admin.site.register(Dispositivo)
admin.site.register(EventoPIR)
admin.site.register(ComandoRemoto)