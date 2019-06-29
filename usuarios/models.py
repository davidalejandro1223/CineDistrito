from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import PersonaManager
# Create your models here.
class Persona(AbstractUser):
    pk_cedula = models.IntegerField(primary_key=True)
    i_telefono = models.IntegerField()
    v_direccion = models.CharField(max_length=100)

    objects = PersonaManager()
    
    REQUIRED_FIELDS = ['pk_cedula', 'email']

    class Meta:
        managed = True
        db_table = 'persona'
    
    def __str__(self):
        return str(self.pk_cedula)+'-'+self.first_name+'-'+self.last_name

class Cliente(models.Model):
    fk_persona = models.OneToOneField('Persona', on_delete=models.CASCADE, db_column='fk_persona', primary_key=True)
    i_numpuntos = models.IntegerField()
    i_numtarjeta = models.CharField(max_length=50)
    d_fechapuntos = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'cliente'
    
    def __str__(self):
        return self.fk_persona