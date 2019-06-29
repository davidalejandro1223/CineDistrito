from django.shortcuts import render
from .models import Pelicula, Funcion, FuncionSala
from rest_framework import viewsets
from .serializers import *

# Create your views here.

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class FuncionViewSet(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FuncionPostSerializer
        elif self.request.method == 'GET':
            return FuncionGetSerializer

class FuncionSalaViewSet(viewsets.ModelViewSet):
    queryset = FuncionSala.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FuncionSalaPostSerializer
        elif self.request.method == 'GET':
            return FuncionSalaGetSerializer