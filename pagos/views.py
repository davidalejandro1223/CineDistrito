from django.shortcuts import render
from reservas.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class Factura(APIView):
    def get(self, request, pk_reserva):
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
    
        subtotal = precio_general+precio_preferencial+precio_snacks
        iva = subtotal*0.19
        total = subtotal+iva
        return Response({
            'precio_general':precio_general,
            'precio_preferencial':precio_general,
            'precio_snacks':precio_snacks,
            'subtotal':subtotal,
            'iva':iva,
            'total':total
        })