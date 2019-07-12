from rest_framework import serializers
from .models import SillaReservada
from multiplex.serializers import SillaGetSerializer
class SillaReservadaSerializer(serializers.ModelSerializer):
    fk_silla = SillaGetSerializer()
    class Meta:
        model = SillaReservada
        fields = ('v_estado','fk_silla' )