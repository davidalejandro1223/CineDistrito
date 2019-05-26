# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    fk_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='fk_persona', primary_key=True)
    i_numpuntos = models.IntegerField()
    i_numtarjeta = models.CharField(max_length=50)
    d_fechapuntos = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'


class Contrato(models.Model):
    id = models.IntegerField(primary_key=True)
    v_tipocontrato = models.CharField(max_length=100)
    d_iniciocontrato = models.DateField()
    i_salario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contrato'


class Empleado(models.Model):
    fk_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='fk_persona', primary_key=True)
    fk_contrato = models.IntegerField()
    n_descuento = models.DecimalField(max_digits=4, decimal_places=2)
    fk_numcontrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='fk_numcontrato', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class EmpleadoMultiplex(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='fk_empleado')
    fk_multiplex = models.ForeignKey('Multiplex', models.DO_NOTHING, db_column='fk_multiplex')
    f_transferencia = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'empleado_multiplex'


class Funcion(models.Model):
    id = models.AutoField(primary_key=True)
    v_estado = models.CharField(max_length=50)
    d_proyeccion = models.DateField()
    fk_pelicula = models.ForeignKey('Pelicula', models.DO_NOTHING, db_column='fk_pelicula')
    t_inicioproyeccion = models.TimeField()
    t_finproyeccion = models.TimeField()

    class Meta:
        managed = True
        db_table = 'funcion'


class Multiplex(models.Model):
    id = models.IntegerField(primary_key=True)
    v_nombre = models.CharField(max_length=100)
    v_direccion = models.CharField(max_length=100)
    v_ciudad = models.CharField(max_length=100)
    i_minsalas = models.IntegerField()
    i_maxsalas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'multiplex'


class Pago(models.Model):
    pk_numpago = models.IntegerField(primary_key=True)
    t_fechapago = models.DateTimeField()
    i_subtotalpago = models.IntegerField()
    i_totalpago = models.IntegerField()
    i_puntosganados = models.IntegerField()
    v_metodopago = models.CharField(max_length=50)
    fk_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='fk_cliente')
    fk_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='fk_reserva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Pelicula(models.Model):
    id = models.IntegerField(primary_key=True)
    v_nombre = models.CharField(max_length=150)
    i_duracion = models.IntegerField()
    tx_sinapsis = models.TextField()
    v_foto = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'pelicula'


class Persona(models.Model):
    pk_cedula = models.IntegerField(primary_key=True)
    v_primernombre = models.CharField(max_length=100)
    v_segundonombre = models.CharField(max_length=100, blank=True, null=True)
    v_primerapellido = models.CharField(max_length=100)
    v_segundoapellido = models.CharField(max_length=100)
    i_telefono = models.IntegerField()
    v_direccion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'persona'


class Reserva(models.Model):
    id = models.IntegerField(primary_key=True)
    v_estado = models.CharField(max_length=50)
    t_inicioreserva = models.TimeField()
    fk_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='fk_persona')

    class Meta:
        managed = False
        db_table = 'reserva'


class Sala(models.Model):
    id = models.IntegerField(primary_key=True)
    i_numpreferencial = models.IntegerField()
    i_numgeneral = models.IntegerField()
    fk_multiplex = models.ForeignKey(Multiplex, models.DO_NOTHING, db_column='fk_multiplex')

    class Meta:
        managed = False
        db_table = 'sala'
        unique_together = (('id', 'fk_multiplex'),)


class Silla(models.Model):
    pk_numero = models.CharField(primary_key=True, max_length=3)
    fk_sala = models.ForeignKey(Sala, models.DO_NOTHING, db_column='fk_sala')
    v_tipo = models.CharField(max_length=50)
    i_orden = models.CharField(max_length=50)
    fk_multiplex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'silla'
        unique_together = (('pk_numero', 'fk_sala', 'fk_multiplex'),)


class SillaFuncion(models.Model):
    id = models.IntegerField(primary_key=True)
    v_estado = models.CharField(max_length=50)
    fk_silla = models.ForeignKey(Silla, models.DO_NOTHING, db_column='fk_silla')
    fk_funcion = models.ForeignKey(Funcion, models.DO_NOTHING, db_column='fk_funcion')
    fk_sala = models.IntegerField()
    fk_multiplex = models.IntegerField()
    fk_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='fk_reserva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'silla_funcion'


class Snack(models.Model):
    id = models.IntegerField(primary_key=True)
    v_tipo = models.CharField(max_length=50)
    v_nombre = models.CharField(max_length=50)
    tx_descripcion = models.TextField()
    i_precio = models.IntegerField()
    i_puntosofrecidos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snack'


class SnackReserva(models.Model):
    fk_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='fk_reserva')
    fk_snack = models.ForeignKey(Snack, models.DO_NOTHING, db_column='fk_snack', primary_key=True)
    i_cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'snack_reserva'
        unique_together = (('fk_snack', 'fk_reserva'),)
