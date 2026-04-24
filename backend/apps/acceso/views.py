from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.usuarios.models import Usuario, TarjetaRFID, UsuarioRol
from apps.organizacion.models import PuertaAcceso
from .models import PermisoAcceso, IntentoAcceso, EstadoPuerta
from .serializer import (
    PermisoAccesoSerializer,
    IntentoAccesoSerializer,
    EstadoPuertaSerializer
)

# =========================
# CRUD (VIEWSETS)
# =========================

class PermisoAccesoViewSet(viewsets.ModelViewSet):
    queryset = PermisoAcceso.objects.all()
    serializer_class = PermisoAccesoSerializer


class IntentoAccesoViewSet(viewsets.ModelViewSet):
    queryset = IntentoAcceso.objects.all()
    serializer_class = IntentoAccesoSerializer


class EstadoPuertaViewSet(viewsets.ModelViewSet):
    queryset = EstadoPuerta.objects.all()
    serializer_class = EstadoPuertaSerializer


# =========================
# ENDPOINT IoT (NO TOCAR)
# =========================

@api_view(['POST'])
def validar_acceso(request):
    uid = request.data.get('uid')
    puerta_id = request.data.get('puerta_id')

    try:
        tarjeta = TarjetaRFID.objects.get(uid=uid, estado=True)
        usuario = tarjeta.usuario

        roles = UsuarioRol.objects.filter(usuario=usuario).values_list('rol_id', flat=True)

        permisos = PermisoAcceso.objects.filter(
            rol_id__in=roles,
            puerta_acceso_id=puerta_id,
            estado=True
        )

        if permisos.exists():
            resultado = "PERMITIDO"
            acceso = True
        else:
            resultado = "DENEGADO"
            acceso = False

        IntentoAcceso.objects.create(
            usuario=usuario,
            puerta_acceso_id=puerta_id,
            tarjeta_rfid=tarjeta,
            resultado=resultado,
            motivo="OK" if acceso else "SIN PERMISO"
        )

        return Response({
            "acceso": acceso,
            "mensaje": resultado
        })

    except TarjetaRFID.DoesNotExist:

        IntentoAcceso.objects.create(
            usuario=None,
            puerta_acceso_id=puerta_id,
            resultado="DENEGADO",
            motivo="TARJETA INVALIDA"
        )

        return Response({
            "acceso": False,
            "mensaje": "TARJETA INVALIDA"
        }, status=status.HTTP_404_NOT_FOUND)