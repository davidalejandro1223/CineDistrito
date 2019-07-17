from django.contrib.auth.models import UserManager
from django.db import models

class EmpleadoManager(models.Manager):
    
    def __init__(self, persona, *args, **kwargs):
        self.persona = persona
        return super().__init__(*args, **kwargs)
    
    def create(self, email,username, pk_cedula, i_telefono, v_direccion, first_name, last_name, descuento, contrato, password=None):
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
        
        empleado = self.model(
            fk_persona=persona,
            n_descuento=descuento,
            fk_numcontrato=contrato   
        )
        empleado.save()
        return empleado