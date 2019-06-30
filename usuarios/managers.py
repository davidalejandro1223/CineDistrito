from django.contrib.auth.models import UserManager
from django.db import models
from random import randint

class PersonaManager(UserManager):
    def create_user(self, email,username, pk_cedula, i_telefono, v_direccion, first_name, last_name, password=None):
        if not email:
            raise ValueError("Debe ingresar un correo electronico")
        
        user = self.model(
            email=self.normalize_email(email), 
            username=username, 
            pk_cedula=pk_cedula, 
            i_telefono=i_telefono, 
            v_direccion=v_direccion, 
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff = False,
            is_superuser = False,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, cedula, password):
        user = self.create_user(
            cedula = cedula,
            password=password
        )
        user.staf = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,username, pk_cedula, password):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            pk_cedula = pk_cedula,
            i_telefono = 00000,
            v_direccion = 'superuser no aplica',
            is_staff = True,
            is_superuser = True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class ClienteManager(models.Manager):

    def __init__(self, persona, *args, **kwargs):
        self.persona = persona
        return super().__init__(*args, **kwargs)
    
    def create(self, email,username, pk_cedula, i_telefono, v_direccion, first_name, last_name, password=None):
        persona = self.persona.objects.create_user(
            email=email, 
            username=username, 
            pk_cedula=pk_cedula, 
            i_telefono=i_telefono, 
            v_direccion=v_direccion, 
            password=password,
            first_name=first_name,
            last_name=last_name,
            )
        
        cliente = self.model(
            fk_persona=persona,
            i_numpuntos = 0,
            i_numtarjeta = randint(1000000, 10000000),
            d_fechapuntos = None
        )
        cliente.save()
        return cliente