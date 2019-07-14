from rest_framework import serializers
from .models import SillaReservada, SnackReserva, Reserva, Pago
from multiplex.serializers import SillaGetSerializer
from snacks.serializers import SnackSerializer

class SillaReservadaSerializer(serializers.ModelSerializer):
    fk_silla = SillaGetSerializer()
    class Meta:
        model = SillaReservada
        fields = ('v_estado','fk_silla' )

class SnackReservaGetSerializer(serializers.ModelSerializer):
    fk_snack = SnackSerializer()
    class Meta:
        model = SnackReserva
        fields = '__all__'

class SnackReservaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnackReserva
        fields = '__all__'

class ReservaGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'