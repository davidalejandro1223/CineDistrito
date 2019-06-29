from __future__ import unicode_literals
from django.contrib import admin
from .models import Funcion, Pelicula, FuncionSala


# Register your models here.

@admin.register(Funcion)
class AdminFuncion(admin.ModelAdmin):
    list_display = ('id', 'v_estado', 'd_proyeccion', 'fk_pelicula', 't_inicioproyeccion', 't_finproyeccion')

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'v_nombre', 'i_duracion')

@admin.register(FuncionSala)
class FuncionSalaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_funcion', 'fk_sala')
