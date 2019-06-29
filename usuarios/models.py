from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Persona(AbstractUser):
    pk_cedula = models.IntegerField(primary_key=True)
    v_primernombre = models.CharField(max_length=100)
    v_segundonombre = models.CharField(max_length=100, blank=True, null=True)
    v_primerapellido = models.CharField(max_length=100)
    v_segundoapellido = models.CharField(max_length=100)
    i_telefono = models.IntegerField()
    v_direccion = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'persona'

class Cliente(models.Model):
    fk_persona = models.OneToOneField('Persona', models.DO_NOTHING, db_column='fk_persona', primary_key=True)
    i_numpuntos = models.IntegerField()
    i_numtarjeta = models.CharField(max_length=50)
    d_fechapuntos = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'