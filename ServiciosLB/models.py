
from enum import auto
from tabnanny import verbose
from django.db import models

# Create your models here.
# base de datos

class historialregistro (models.Model):
    cliente_host= models.CharField(max_length=50)
    dire_ip=models.CharField(max_length=50)
    dire_puerto=models.CharField(max_length=50)
    vulnerabilidad=models.CharField(max_length=200)
    fecha_scaneo=models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'escaneo'
        verbose_name_plural ='escaneos'
    
    # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return self.cliente_host
