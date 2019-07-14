from django.db import models
from multiplex.models import Silla
from funciones.models import FuncionSala
from usuarios.models import Persona, Cliente
from snacks.models import Snack
# Create your models here.

class Reserva(models.Model):
    v_estado = models.CharField(max_length=50)
    t_inicioreserva = models.TimeField(auto_now=True)
    fk_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='fk_persona')

    class Meta:
        managed = True
        db_table = 'reserva'

    def __str__(self):
        return str(self.id)

class SillaReservada(models.Model):
    estados = (('proceso', 'En proceso'), 
                ('reservada', 'Reservada'))
    v_estado = models.CharField(max_length=50, choices=estados)
    fk_silla = models.ForeignKey(Silla, on_delete=models.CASCADE, db_column='fk_silla')
    fk_funcion_sala = models.ForeignKey(FuncionSala, on_delete=models.CASCADE, db_column='fk_funcion_sala', related_name='funsalas')
    fk_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, db_column='fk_reserva')

    class Meta:
        managed = True
        db_table = 'silla_reservada'
    
    def __str__(self):
        return str(self.fk_silla) + '-' +  str(self.fk_reserva)

class SnackReserva(models.Model):
    fk_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, db_column='fk_reserva')
    fk_snack = models.ForeignKey(Snack, on_delete=models.CASCADE, db_column='fk_snack')
    i_cantidad = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'snack_reserva'
    
    def __str__(self):
        return str(self.id) + '-' +  self.fk_reserva

class Pago(models.Model):
    pk_numpago = models.AutoField(primary_key=True)
    t_fechapago = models.DateTimeField()
    i_subtotalpago = models.IntegerField()
    i_totalpago = models.IntegerField()
    i_puntosganados = models.IntegerField()
    v_metodopago = models.CharField(max_length=50)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='fk_cliente')
    fk_reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE, db_column='fk_reserva', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pago'

    def __str__(self):
        return str(self.pk_numpago) + '-' +  self.fk_reserva