from django.db import models

# Create your models here.
class Multiplex(models.Model):
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    i_numpreferencial = models.IntegerField()
    i_numgeneral = models.IntegerField()
    fk_multiplex = models.ForeignKey(Multiplex, on_delete=models.CASCADE, db_column='fk_multiplex')

    def __str__(self):
        return self.id
    

    class Meta:
        managed = False
        db_table = 'sala'
        unique_together = (('id', 'fk_multiplex'),)
    
class Silla(models.Model):
    pk_numero = models.CharField(primary_key=True, max_length=3)
    fk_sala = models.ForeignKey(Sala, on_delete=models.CASCADE, db_column='fk_sala')
    v_tipo = models.CharField(max_length=50)
    i_orden = models.CharField(max_length=50)
    fk_multiplex = models.ForeignKey(Multiplex, on_delete=models.CASCADE, db_column='fk_multiplex')

    def __str__(self):
        return self.pk_numero
    

    class Meta:
        managed = False
        db_table = 'silla'
        unique_together = (('pk_numero', 'fk_sala', 'fk_multiplex'),)