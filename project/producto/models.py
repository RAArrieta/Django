from django.db import models

# Create your models here.

class Categoria(models.Model):
    """Categoria de los productos"""
    nombre = models.CharField(max_length=200, unique=True)
    # unique asegura que no se repita
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    # null y blank en conjunto permiten que sea opcional el campo

    def __str__(self) -> str:
        return self.nombre

# class Producto(models.Model):
#     nombre = models.CharField(max_length=200)
#     precio = models.CharField()

