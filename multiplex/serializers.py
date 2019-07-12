from rest_framework import serializers
from .models import Multiplex, Sala, Silla

class MultiplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multiplex
        fields = (
            'id', 
            'v_nombre', 
            'v_direccion',
            'v_ciudad',
            'i_minsalas',
            'i_maxsalas'
        )


class SalaGetSerializer(serializers.ModelSerializer):
    fk_multiplex = MultiplexSerializer()
    class Meta:
        model = Sala
        fields = (
            'id',
            'i_numsala',
            'i_numpreferencial',
            'i_numgeneral',
            'fk_multiplex'
        )

class SalaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = (
            'i_numsala',
            'i_numpreferencial',
            'i_numgeneral',
            'fk_multiplex'
        )

class SillaGetSerializer(serializers.ModelSerializer):
    fk_sala = SalaGetSerializer()
    class Meta:
        model = Silla
        fields = (
            'id',
            'pk_numero',
            'fk_sala',
            'v_tipo',
            'i_orden',
        )

class SillaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silla
        fields = (
            'id',
            'pk_numero',
            'fk_sala',
            'v_tipo',
            'i_orden',
        )