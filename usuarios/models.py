from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    puntos = models.IntegerField(default=0)
    is_admin= models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Hashear la contraseña antes de guardarla
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def verificar_contrasena(self, contrasena):
        # Verificar la contraseña utilizando el método check_password de Django
        return check_password(contrasena, self.password)
