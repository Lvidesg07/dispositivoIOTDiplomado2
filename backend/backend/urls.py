from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# usuarios
from apps.usuarios.views import (
    UsuarioViewSet,
    RolViewSet,
    UsuarioRolViewSet,
    TarjetaRFIDViewSet
)

# organizacion
from apps.organizacion.views import (
    OrganizacionViewSet,
    SedeViewSet,
    ZonaViewSet,
    PuertaAccesoViewSet
)

# dispositivos
from apps.dispositivos.views import (
    DispositivoViewSet,
    EventoPIRViewSet,
    ComandoRemotoViewSet
)

# acceso
from apps.acceso.views import (
    PermisoAccesoViewSet,
    IntentoAccesoViewSet,
    EstadoPuertaViewSet,
    validar_acceso
)

# auditoria
from apps.auditoria.views import AuditoriaViewSet


router = DefaultRouter()

# usuarios
router.register(r'usuarios', UsuarioViewSet)
router.register(r'roles', RolViewSet)
router.register(r'usuario-roles', UsuarioRolViewSet)
router.register(r'tarjetas', TarjetaRFIDViewSet)

# organizacion
router.register(r'organizaciones', OrganizacionViewSet)
router.register(r'sedes', SedeViewSet)
router.register(r'zonas', ZonaViewSet)
router.register(r'puertas', PuertaAccesoViewSet)

# dispositivos
router.register(r'dispositivos', DispositivoViewSet)
router.register(r'eventos-pir', EventoPIRViewSet)
router.register(r'comandos', ComandoRemotoViewSet)

# acceso
router.register(r'permisos', PermisoAccesoViewSet)
router.register(r'intentos', IntentoAccesoViewSet)
router.register(r'estado-puertas', EstadoPuertaViewSet)

# auditoria
router.register(r'auditoria', AuditoriaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # endpoint IoT
    path('api/validar-acceso/', validar_acceso),
]