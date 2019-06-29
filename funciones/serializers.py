from .models import Pelicula, Funcion, FuncionSala
from rest_framework import serializers
from multiplex.serializers import SalaGetSerializer

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ('id', 'v_nombre', 'i_duracion', 'tx_sinapsis', 'v_foto')

class FuncionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcion
        fields = ('v_estado', 'd_proyeccion', 'fk_pelicula', 't_inicioproyeccion', 't_finproyeccion')

class FuncionGetSerializer(serializers.ModelSerializer):
    fk_pelicula = PeliculaSerializer()
    class Meta:
        model = Funcion
        fields = ('id', 'v_estado', 'd_proyeccion', 'fk_pelicula', 't_inicioproyeccion', 't_finproyeccion')

class FuncionSalaGetSerializer(serializers.ModelSerializer):
    fk_funcion = FuncionGetSerializer()
    fk_sala = SalaGetSerializer()

    class Meta:
        model = FuncionSala
        fields = '__all__'

class FuncionSalaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionSala
        fields = '__all__'