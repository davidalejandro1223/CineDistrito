from django.contrib import admin
from .models import Pago
# Register your models here.
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('pk_numpago', 'fk_cliente', 'fk_reserva', 't_fechapago', 'i_totalpago')