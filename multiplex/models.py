from django.db import models

# Create your models here.
class Multiplex(models.Model):
    v_nombre = models.CharField(max_length=100)
    v_direccion = models.CharField(max_length=100)
    v_ciudad = models.CharField(max_length=100)
    i_minsalas = models.IntegerField()
    i_maxsalas = models.IntegerField()

    def __str__(self):
        return self.v_nombre
    

    class Meta:
        db_table = 'multiplex'
        managed = False

class Sala(models.Model):
    i_numsala = models.IntegerField()
    i_numpreferencial = models.IntegerField()
    i_numgeneral = models.IntegerField()
    fk_multiplex = models.ForeignKey(Multiplex,on_delete=models.CASCADE, db_column='fk_multiplex')

    def __str__(self):
        return self.fk_multiplex.v_nombre+'-'+str(self.i_numsala)
    

    class Meta:
        managed = False
        db_table = 'sala'
        unique_together = (('i_numsala', 'fk_multiplex'),)
    
class Silla(models.Model):
    tipo_silla = (('preferencial','Preferencial'), 
                    ('general','General'))
                    
    pk_numero = models.CharField(max_length=3)
    fk_sala = models.ForeignKey(Sala, on_delete=models.CASCADE, db_column='fk_sala')
    v_tipo = models.CharField(max_length=50, choices=tipo_silla)
    i_orden = models.CharField(max_length=50)

    def __str__(self):
        return str(self.fk_sala)+'-'+str(self.pk_numero)
    

    class Meta:
        managed = False
        db_table = 'silla'
        unique_together = (('pk_numero', 'fk_sala'),)