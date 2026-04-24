from rest_framework import viewsets
from .models import Organizacion, Sede, Zona, PuertaAcceso
from .serializer import (
    OrganizacionSerializer,
    SedeSerializer,
    ZonaSerializer,
    PuertaAccesoSerializer
)


class OrganizacionViewSet(viewsets.ModelViewSet):
    queryset = Organizacion.objects.all()
    serializer_class = OrganizacionSerializer


class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer


class PuertaAccesoViewSet(viewsets.ModelViewSet):
    queryset = PuertaAcceso.objects.all()
    serializer_class = PuertaAccesoSerializer