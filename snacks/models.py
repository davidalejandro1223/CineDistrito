from django.db import models

# Create your models here.
class Snack(models.Model):
    v_tipo = models.CharField(max_length=50)
    v_nombre = models.CharField(max_length=50)
    tx_descripcion = models.TextField()
    i_precio = models.IntegerField()
    i_puntosofrecidos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snack'
    
    def __str__(self):
        return str(self.id)+'-'+self.v_nombre