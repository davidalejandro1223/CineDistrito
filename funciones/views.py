from django.shortcuts import render
from .models import Pelicula, Funcion
from rest_framework import viewsets
from .serializers import PeliculaSerializer, FuncionGetSerializer, FuncionPostSerializer

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