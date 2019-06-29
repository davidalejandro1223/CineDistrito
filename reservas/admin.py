from django.contrib import admin
from .models import Reserva, SillaReservada, SnackReserva, Pago
# Register your models here.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'v_estado', 'fk_persona')

@admin.register(SillaReservada)
class SillaReservadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_silla', 'fk_funcion_sala', 'fk_reserva')

@admin.register(SnackReserva)
class SnackReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_reserva', 'fk_snack', 'i_cantidad')

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('pk_numpago', 'fk_cliente', 'fk_reserva', 't_fechapago', 'i_totalpago')