from django.db import models

class Post(models.Model):
    nombre_animal = models.CharField(max_length=30)
    tipo_animal = models.CharField(max_length=80)
    edad_animal = models.CharField(max_length=15)
    pre_diagnostico = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id} - {self.tipo_animal}"
    
# Create your models here.
