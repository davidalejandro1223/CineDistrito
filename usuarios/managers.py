from django.contrib.auth.models import UserManager 

class PersonaManager(UserManager):
    def create_user(self, email, cedula, password=None):
        if not email:
            raise ValueError("Debe ingresar un correo electronico")
        
        user = self.model(
            email = self.normalize_email(email),
            pk_cedula = cedula
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