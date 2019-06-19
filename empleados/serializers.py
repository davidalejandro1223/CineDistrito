from .models import Contrato
from rest_framework import serializers

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'
