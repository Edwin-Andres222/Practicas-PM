from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 255);
    apellido = models.CharField(max_length = 255);
    correoElectronico = models.CharField(max_length = 255);
    fechaIngreso = models.DateField();

    def __str__(self) -> str:
        return f'Usuario {self.id}: {self.nombre} {self.apellido}';