from __future__ import unicode_literals
from django.contrib import admin
from .models import Multiplex, Sala, Silla

# Register your models here.

@admin.register(Multiplex)
class MultiplexAdmin(admin.ModelAdmin):
    list_display = ('id', 'v_nombre', 'v_ciudad')

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('id', 'i_numsala','fk_multiplex')

@admin.register(Silla)
class SillaAdmin(admin.ModelAdmin):
    list_display = ('id','pk_numero', 'fk_sala')



