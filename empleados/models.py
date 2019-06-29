from django.db import models
from usuarios.models import Persona
from multiplex.models import Multiplex

# Create your models here.
class Contrato(models.Model):
    id = models.IntegerField(primary_key=True)
    v_tipocontrato = models.CharField(max_length=100)
    d_iniciocontrato = models.DateField()
    i_salario = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'contrato'

class Empleado(models.Model):
    fk_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, db_column='fk_persona', primary_key=True)
    fk_contrato = models.IntegerField()
    n_descuento = models.DecimalField(max_digits=4, decimal_places=2)
    fk_numcontrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, db_column='fk_numcontrato')

    class Meta:
        managed = True
        db_table = 'empleado'

class EmpleadoMultiplex(models.Model):
    fk_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='fk_empleado')
    fk_multiplex = models.ForeignKey(Multiplex, on_delete=models.CASCADE, db_column='fk_multiplex')
    f_transferencia = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'empleado_multiplex'
