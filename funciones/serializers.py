from .models import Pelicula, Funcion
from rest_framework import serializers

class PeliculaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pelicula
        fields = ('id', 'v_nombre', 'i_duracion', 'tx_sinapsis', 'v_foto')

class FuncionSerializer(serializers.HyperlinkedModelSerializer):
    fk_pelicula = PeliculaSerializer()
    class Meta:
        model = Funcion
        fields = ('id', 'v_estado', 'd_proyeccion', 'fk_pelicula', 't_inicioproyeccion', 't_finproyeccion')
