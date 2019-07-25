from django.shortcuts import render
from reservas.models import *
from usuarios.models import Cliente
from empleados.models import Empleado
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Pago

# Create your views here.

class FacturaView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk_reserva):
        cliente = Cliente.objects.get(fk_persona=request.user)

        calculo_factura = self.calculo_factura(pk_reserva,cliente)           
            
        return Response({
            'precio_general':calculo_factura['precio_general'],
            'precio_preferencial':calculo_factura['precio_preferencial'],
            'precio_snacks':calculo_factura['precio_snacks'],
            'subtotal':calculo_factura['subtotal'],
            'iva':calculo_factura['iva'],
            'total':calculo_factura['total'],
            'puntos_acumulados':calculo_factura['puntos_acumulados'],
        })
    
    def calculo_factura(self, pk_reserva, cliente):
        boletas = SillaReservada.objects.filter(fk_reserva=pk_reserva)
        snacks = SnackReserva.objects.filter(fk_reserva=pk_reserva)
        
        precio_general = 0
        precio_preferencial = 0
        precio_snacks = 0
        puntos_ganados = 0
        puntos_acumulados = cliente.i_numpuntos

        for boleta in boletas:
            puntos_ganados+=10
            if boleta.fk_silla.v_tipo == 'general':
                precio_general = precio_general+11000
            elif boleta.fk_silla.v_tipo == 'preferencial':
                precio_preferencial = precio_preferencial+15000
        
        for snack in snacks:
            puntos_ganados+=5
            precio_snacks = precio_snacks+(snack.i_cantidad*snack.fk_snack.i_precio)

        subtotal = precio_general+precio_preferencial+precio_snacks

        if puntos_acumulados>100:
            subtotal=subtotal-11000

        try:
            empleado = Empleado.objects.get(fk_persona=cliente.fk_persona)
            descuento= empleado.n_descuento
            subtotal=subtotal-(subtotal*(descuento/100))
        except:
            print('el cliente no es empleado')
        
        iva = subtotal*0.19
        total = subtotal+iva
        return {
            'precio_general':precio_general,
            'precio_preferencial':precio_preferencial,
            'precio_snacks':precio_snacks,
            'subtotal':subtotal,
            'iva':iva,
            'total':total,
            'puntos_acumulados':puntos_acumulados,
            'puntos_ganados':puntos_ganados
        }


class PagoView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk_reserva):
        reserva = Reserva.objects.get(id=pk_reserva)
        cliente = Cliente.objects.get(fk_persona=request.user)
        metodo_pago = request.data['v_metodopago']
        puntos_acumulados = cliente.i_numpuntos

        try:
            factura = FacturaView()
            info_factura = factura.calculo_factura(pk_reserva, cliente)
            
            if puntos_acumulados>100:
                cliente.i_numpuntos=puntos_acumulados-100
                cliente.save()

            pago = Pago(
                i_subtotalpago=info_factura['subtotal'],
                i_totalpago=info_factura['total'],
                i_puntosganados=info_factura['puntos_ganados'],
                v_metodopago=metodo_pago,
                fk_cliente=cliente,
                fk_reserva=reserva
            )

            pago.save()

            sillas = SillaReservada.objects.filter(fk_reserva=pk_reserva)
            for silla in sillas:
                silla.v_estado = 'reservada'
                silla.save()
            
            return Response('El pago se ha realizado satisfactoriamente')
        except:
            return Response('Ha ocurrido un error con el pago, intentelo nuevamente')