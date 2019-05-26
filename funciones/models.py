from django.db import models

# Create your models here.

class Funcion(models.Model):
    id = models.IntegerField(primary_key=True)
    v_estado = models.CharField('estado de la funcion', max_length=50)
    d_proyeccion = models.DateField('dia de proyeccion')
    fk_pelicula = models.ForeignKey(
        'Pelicula', 
        on_delete=models.CASCADE, 
        db_column='fk_pelicula',
        verbose_name='pelicula de la funcion'
    )
    t_inicioproyeccion = models.TimeField('hora de inicio')
    t_finproyeccion = models.TimeField('hora de finalizacion')

    def __str__(self):
        return str(self.id)
    

    class Meta:
        managed = False
        db_table = 'funcion'

class Pelicula(models.Model):
    id = models.IntegerField(primary_key=True)
    v_nombre = models.CharField('nombre pelicula',max_length=150)
    i_duracion = models.IntegerField('duracion pelicula')
    tx_sinapsis = models.TextField('sinapsis pelicula')
    v_foto = models.ImageField('foto pelicula', upload_to='fotos-peliculas/')

    def __str__(self):
        return self.v_nombre
    

    class Meta:
        managed = False
        db_table = 'pelicula'