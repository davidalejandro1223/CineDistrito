from django.shortcuts import render
from .models import Multiplex, Sala, Silla
from rest_framework import viewsets
from .serializers import MultiplexSerializer, SalaSerializer, SillaSerializer
# Create your views here.

class MultiplexViewSet(viewsets.ModelViewSet):
    queryset = Multiplex.objects.all()
    serializer_class = MultiplexSerializer

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class SillaViewSet(viewsets.ModelViewSet):
    queryset = Silla.objects.all()
    serializer_class = SillaSerializer