from django.shortcuts import render
from multiplex.models import Silla
from multiplex.serializers import SillaGetSerializer
from funciones.models import FuncionSala
from .models import SillaReservada
from .serializers import SillaReservadaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class DisponibilidadSillas(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk_sala, pk_funcion, format=None):
        sillas_sala = Silla.objects.filter(fk_sala=pk_sala)
        funcion_sala = FuncionSala.objects.filter(fk_sala=pk_sala).get(fk_funcion=pk_funcion)
        sillas_res = funcion_sala.funsalas.all().filter(v_estado='reservada')
        sillas_prcs = funcion_sala.funsalas.all().filter(v_estado='proceso')
        sillas_dis = sillas_sala.exclude(id__in=sillas_res.values('fk_silla')).exclude(id__in=sillas_prcs.values('fk_silla'))
        serializer_res = SillaReservadaSerializer(sillas_res, many=True)
        serializer_prcs = SillaReservadaSerializer(sillas_prcs, many=True)
        serializer_dis = SillaGetSerializer(sillas_dis, many=True)
        
        return Response({'reservadas':serializer_res.data, 'proceso':serializer_prcs.data, 'disponible':serializer_dis.data})