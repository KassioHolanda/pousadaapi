from rest_framework import serializers

from core.models import Quarto, Reserva


class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = '__all__'


class ReservaSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')
