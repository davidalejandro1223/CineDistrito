from rest_framework import serializers
from .models import Multiplex, Sala, Silla

class MultiplexSerializer(serializers.HyperlinkedModelSerializer):
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

class SalaSerializer(serializers.HyperlinkedModelSerializer):
    fk_multiplex = MultiplexSerializer()
    class Meta:
        model = Sala
        fields = (
            'id',
            'i_numpreferencial',
            'i_numgeneral',
            'fk_multiplex'
        )

class SillaSerializer(serializers.HyperlinkedModelSerializer):
    fk_sala = SalaSerializer()
    fk_multiplex = MultiplexSerializer()
    class Meta:
        model = Silla
        fields = (
            'pk_numero',
            'fk_sala',
            'v_tipo'
            'i_orden',
            'fk_multiplex'
        )