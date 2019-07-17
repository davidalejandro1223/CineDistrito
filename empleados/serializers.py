from .models import Contrato, Empleado
from rest_framework import serializers
from usuarios.serializers import BasicCreatePersonaSerializer, BasicListPersonaSerializer

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class BasicCreateEmpleadoSerializer(serializers.ModelSerializer):
    fk_persona = BasicCreatePersonaSerializer()

    class Meta:
        model = Empleado
        fields = '__all__'
    
    def create(self, validated_data):
        return Empleado.objects.create(
            email=validated_data['fk_persona']['email'],
            username=validated_data['fk_persona']['username'],
            pk_cedula=validated_data['fk_persona']['pk_cedula'],
            i_telefono=validated_data['fk_persona']['i_telefono'],
            v_direccion=validated_data['fk_persona']['v_direccion'],
            first_name=validated_data['fk_persona']['first_name'],
            last_name=validated_data['fk_persona']['last_name'],
            password=validated_data['fk_persona']['password'],
            descuento=validated_data['n_descuento'],
            contrato=validated_data['fk_numcontrato']
        )

class BasicListEmpleadoSerializer(serializers.ModelSerializer):
    fk_persona = BasicListPersonaSerializer()

    class Meta:
        model = Empleado
        fields = '__all__'

