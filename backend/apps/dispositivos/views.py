from rest_framework import viewsets
from .models import Dispositivo, EventoPIR, ComandoRemoto
from .serializer import (
    DispositivoSerializer,
    EventoPIRSerializer,
    ComandoRemotoSerializer
)


class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer


class EventoPIRViewSet(viewsets.ModelViewSet):
    queryset = EventoPIR.objects.all()
    serializer_class = EventoPIRSerializer


class ComandoRemotoViewSet(viewsets.ModelViewSet):
    queryset = ComandoRemoto.objects.all()
    serializer_class = ComandoRemotoSerializer