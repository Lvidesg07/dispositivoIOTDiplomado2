from rest_framework import serializers
from .models import Organizacion, Sede, Zona, PuertaAcceso

class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'


class PuertaAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuertaAcceso
        fields = '__all__'