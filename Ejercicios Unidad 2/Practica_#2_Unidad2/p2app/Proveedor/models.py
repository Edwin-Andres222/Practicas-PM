from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=255);
    apellido = models.CharField(max_length = 255);
    email = models.EmailField();
    compania = models.CharField(max_length=255);

    def __str__(self) -> str:
        return f'Proveedor {self.id}: {self.nombre} {self.apellido} {self.compania}';