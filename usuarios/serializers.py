from .models import Persona, Cliente
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class BasicCreatePersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('pk_cedula', 
                'i_telefono', 
                'v_direccion', 
                'username',
                'email',
                'first_name',
                'last_name',
                'password')
class BasicCreateClienteSerializer(serializers.ModelSerializer):
    fk_persona = BasicCreatePersonaSerializer()

    class Meta:
        model = Cliente
        fields = ('fk_persona',)
    
    def create(self, validated_data):
        return Cliente.objects.create(
            email=validated_data['fk_persona']['email'],
            username=validated_data['fk_persona']['username'],
            pk_cedula=validated_data['fk_persona']['pk_cedula'],
            i_telefono=validated_data['fk_persona']['i_telefono'],
            v_direccion=validated_data['fk_persona']['v_direccion'],
            first_name=validated_data['fk_persona']['first_name'],
            last_name=validated_data['fk_persona']['last_name'],
            password=validated_data['fk_persona']['password']

        )
    
class BasicListPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        exclude = ('password',
                'is_superuser',
                'is_staff',
                'groups',
                'user_permissions')

class BasicListClienteSerializer(serializers.ModelSerializer):
    fk_persona = BasicListPersonaSerializer()

    class Meta:
        model = Cliente
        fields = '__all__'