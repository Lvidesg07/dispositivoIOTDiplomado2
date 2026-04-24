from rest_framework import viewsets
from .models import AuditoriaSistema
from .serializer import AuditoriaSerializer


class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaSistema.objects.all()
    serializer_class = AuditoriaSerializer