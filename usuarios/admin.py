from django.contrib import admin
from .models import Persona, Cliente
# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pk_cedula', 'first_name', 'last_name')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fk_persona', 'i_numpuntos', 'd_fechapuntos')