from django.contrib import admin
from .models import Empleado, Contrato, EmpleadoMultiplex
# Register your models here.

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('fk_persona', 'fk_numcontrato', )

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'v_tipocontrato')

@admin.register(EmpleadoMultiplex)
class EmpleadoMultiplexAdmin(admin.ModelAdmin):
    list_display = ('fk_empleado', 'fk_multiplex', 'f_transferencia')
