from django.db import models

# Create your models here.
class Advogado(models.Model):
    nome = models.CharField(max_length=255)
    oab = models.CharField(max_length=20, unique=True)
    ativo = models.BooleanField(default=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome