from rest_framework import viewsets
from .models import Usuario, Rol, UsuarioRol, TarjetaRFID
from .serializer import (
    UsuarioSerializer,
    RolSerializer,
    UsuarioRolSerializer,
    TarjetaRFIDSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UsuarioRolViewSet(viewsets.ModelViewSet):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer


class TarjetaRFIDViewSet(viewsets.ModelViewSet):
    queryset = TarjetaRFID.objects.all()
    serializer_class = TarjetaRFIDSerializer