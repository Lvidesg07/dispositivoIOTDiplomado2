from rest_framework import serializers
from .models import Dispositivo, EventoPIR, ComandoRemoto

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'


class EventoPIRSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoPIR
        fields = '__all__'


class ComandoRemotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComandoRemoto
        fields = '__all__'