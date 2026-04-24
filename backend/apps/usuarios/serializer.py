from rest_framework import serializers
from .models import Usuario, Rol, UsuarioRol, TarjetaRFID

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = '__all__'


class TarjetaRFIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjetaRFID
        fields = '__all__'