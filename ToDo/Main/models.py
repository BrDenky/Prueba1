from django.db import models

# Create your models here.

class To_do(models.Model):
    Titulo = models.CharField(max_length=250, blank=False)  #blank establece que el campo puede o no estár vacío
    Descripcion = models.TextField(blank=True)
    Fecha = models.DateField(blank=False)
    Completado = models.BooleanField(default=False) #blank = False establecerá la tarea como 'No completada'

    def __str__(self):
        return self.Titulo