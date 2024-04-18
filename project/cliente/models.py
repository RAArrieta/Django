from django.db import models

class Pais(models.Model):
    #Charfield solo indica que es un tipo str
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank= True, null=True)
    #on_delete, si se elimina el pais en el cliente figurara NULL
    #blank, hace que el campo no sea obligatorio

    def __str__(self):
        return f"{self.apellido} {self.nombre}"
