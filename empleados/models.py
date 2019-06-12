from django.db import models

# Create your models here.

class Contrato(models.Model):
    id = models.IntegerField(primary_key=True)
    v_tipocontrato = models.CharField(max_length=100)
    d_iniciocontrato = models.DateField()
    i_salario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contrato'