from django.shortcuts import render
from .models import Contrato, Empleado
from rest_framework import viewsets
from .serializers import *

class contratosViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BasicCreateEmpleadoSerializer
        if self.request.method == 'GET':
            return BasicListEmpleadoSerializer
