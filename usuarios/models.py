from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import PersonaManager, ClienteManager

# Create your models here.
class Persona(AbstractUser):
    pk_cedula = models.IntegerField('Cedula',primary_key=True)
    i_telefono = models.BigIntegerField('Telefono')
    v_direccion = models.CharField('Direccion',max_length=100)

    objects = PersonaManager()
    
    REQUIRED_FIELDS = ['pk_cedula', 'email']

    class Meta:
        managed = True
        db_table = 'persona'
    
    def __str__(self):
        return str(self.pk_cedula)

class Cliente(models.Model):
    fk_persona = models.OneToOneField('Persona', on_delete=models.CASCADE, db_column='fk_persona', primary_key=True)
    i_numpuntos = models.IntegerField('Numero de puntos')
    i_numtarjeta = models.CharField('Numero tarjeta preferente',max_length=50)
    d_fechapuntos = models.DateField('fecha expiracion puntos', max_length=50, blank=True, null=True)

    objects = ClienteManager(Persona)

    class Meta:
        managed = True
        db_table = 'cliente'
    
    def __str__(self):
        return str(self.fk_persona.username)

