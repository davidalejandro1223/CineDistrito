from django.shortcuts import render
from multiplex.models import Silla
from multiplex.serializers import SillaGetSerializer
from funciones.models import FuncionSala
from .models import SillaReservada, SnackReserva, Reserva, Pago
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.utils import timezone
import datetime

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
        
        try:
            ultima_reserva_usuario = Reserva.objects.filter(
                fk_persona=request.user
                ).order_by('-t_inicioreserva')[0]

            tiempo_limite = ultima_reserva_usuario.t_inicioreserva + datetime.timedelta(minutes=5)

            if tiempo_limite > timezone.now():
                reserva = ultima_reserva_usuario
            else:
                reserva = Reserva(
                v_estado='en proceso',
                fk_persona=request.user,
                t_inicioreserva = timezone.now().strftime("%Y-%m-%d %H:%M")
                )
                reserva.save()
                if ultima_reserva_usuario.v_estado == 'en proceso':
                    ultima_reserva_usuario.v_estado = 'cancelada'
                    ultima_reserva_usuario.save()
            
        except: 
            reserva = Reserva(
                v_estado='en proceso',
                fk_persona=request.user,
                t_inicioreserva = timezone.now().strftime("%Y-%m-%d %H:%M")
            )
            reserva.save()
        print(reserva.t_inicioreserva)
        serializer_reserva = ReservaGetSerializer(reserva)

        return Response({
            'reservadas':serializer_res.data, 
            'proceso':serializer_prcs.data, 
            'disponible':serializer_dis.data,
            'reserva':serializer_reserva.data,
            'fk_funcion_sala':funcion_sala.id
            })

    def post(self, request, format=None):
        reserva = Reserva.objects.get(id=request.data['fk_reserva'])
        funcion_sala = FuncionSala.objects.get(id=request.data['fk_funcion_sala'])
        silla = Silla.objects.get(id=request.data['fk_silla'])
        
        try:
            ultima_reserva_usuario = Reserva.objects.filter(
                fk_persona=request.user
                ).order_by('-t_inicioreserva')[0]

            tiempo_limite = ultima_reserva_usuario.t_inicioreserva + datetime.timedelta(minutes=5)

            if tiempo_limite > timezone.now():
                try:
                    silla_reservada = SillaReservada.objects.filter(
                        fk_reserva=reserva
                    ).filter(
                        fk_silla=silla
                    ).get(
                        fk_funcion_sala=funcion_sala,
                    )
                except:
                    silla_reservada = None


                if silla_reservada:
                    if request.user == reserva.fk_persona:
                        silla_reservada.delete()
                        return Response('La silla se ha liberado')
                    return Response('La silla se encuentra en proceso de reserva o ya esta reservada')

                silla_reservada = SillaReservada(
                    v_estado='en proceso',
                    fk_silla=silla,
                    fk_funcion_sala=funcion_sala,
                    fk_reserva=reserva 
                    )
                
                silla_reservada.save()
                return Response('La silla se ha bloqueado')
            else:
                return Response('El tiempo para terminar la reserva ha finalizado')
        except:
            return('No tiene ninguna reserva')


class SnackReservaViewSet(ModelViewSet):
    queryset = SnackReserva.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SnackReservaGetSerializer
        elif self.request.method == 'POST':
            return SnackReservaPostSerializer

class Factura(APIView):
    def post(self, request, pk_reserva):
        boletas = SillaReservada.objects.filter(fk_reserva=pk_reserva)
        snacks = SnackReserva.objects.filter(fk_reserva=pk_reserva)
        
        precio_general = 0
        precio_preferencial = 0
        precio_snacks = 0

        for boleta in boletas:
            if boleta.fk_silla.v_tipo == 'general':
                precio_general = precio_general+11000
            elif boleta.fk_silla.v_tipo == 'preferencial':
                precio_preferencial = precio_preferencial+15000
        
        for snack in snacks:
            precio_snacks = precio_snacks+(snack.i_cantidad*snack.fk_snack.i_precio)
        
        print('el precio general es {}, el precio preferencial es {}, el precio snacks es {}'.format(precio_general, precio_preferencial, precio_snacks))

        return Response('el precio general es {}, el precio preferencial es {}, el precio snacks es {}'.format(precio_general, precio_preferencial, precio_snacks))