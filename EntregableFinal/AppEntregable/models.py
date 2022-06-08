from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre+" "+str(self.autor)
