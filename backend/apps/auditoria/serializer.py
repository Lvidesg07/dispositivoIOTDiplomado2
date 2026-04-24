from rest_framework import serializers
from .models import AuditoriaSistema

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaSistema
        fields = '__all__'