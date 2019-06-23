from django.shortcuts import render
from .models import Multiplex, Sala, Silla
from rest_framework import viewsets
from .serializers import *
# Create your views here.

class MultiplexViewSet(viewsets.ModelViewSet):
    queryset = Multiplex.objects.all()
    serializer_class = MultiplexSerializer

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SalaPostSerializer
        elif self.request.method == 'GET':
            return SalaGetSerializer


class SillaViewSet(viewsets.ModelViewSet):
    queryset = Silla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SillaPostSerializer
        elif self.request.method == 'GET':
            return SillaGetSerializer