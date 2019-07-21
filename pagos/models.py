from django.db import models
from usuarios.models import Cliente
from reservas.models import Reserva

# Create your models here.
class Pago(models.Model):
    pk_numpago = models.AutoField(primary_key=True)
    t_fechapago = models.DateTimeField(auto_now=True)
    i_subtotalpago = models.IntegerField()
    i_totalpago = models.IntegerField()
    i_puntosganados = models.IntegerField()
    v_metodopago = models.CharField(max_length=50)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='fk_cliente')
    fk_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, db_column='fk_reserva', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pago'

    def __str__(self):
        return str(self.pk_numpago) + '-' +  self.fk_reserva
    