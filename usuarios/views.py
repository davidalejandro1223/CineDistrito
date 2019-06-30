from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Persona, Cliente
from .serializers import PersonaSerializer, BasicCreateClienteSerializer, BasicListClienteSerializer
from rest_framework.viewsets import ModelViewSet
from django.db import transaction
# Create your views here.

class listPersonas(ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (IsAuthenticated,)

#@transaction.atomic
class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BasicCreateClienteSerializer
        if self.request.method == 'GET':
            return BasicListClienteSerializer
