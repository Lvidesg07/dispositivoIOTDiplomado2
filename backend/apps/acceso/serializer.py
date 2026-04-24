from rest_framework import serializers
from .models import PermisoAcceso, IntentoAcceso, EstadoPuerta

class PermisoAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoAcceso
        fields = '__all__'


class IntentoAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntentoAcceso
        fields = '__all__'


class EstadoPuertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPuerta
        fields = '__all__'