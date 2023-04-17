from django.db import models
from Usuario.models import Usuario
# Create your models here.

class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null = True)
    fecha_publicacion = models.DateField()
    contenido = models.TextField()

def __str__(self):
        return self.contenido