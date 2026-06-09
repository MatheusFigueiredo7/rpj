from django.db import models
from advogados.models import Advogado

class Processo(models.Model):
    status_choices = [
        ("ABERTO", "Aberto"),
        ("EM_ANDAMENTO", "Em andamento"),
        ("CONCLUIDO", "Concluído"),
    ]
    prioridades_choices = [
        ("URGENTE", "Urgente"),
        ("NAO_URGENTE", "Não urgente")
    ]
    
    numero_processo = models.CharField(max_length=20, unique=True)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default="ABERTO")
    prioridade = models.CharField(max_length=20, choices=prioridades_choices, default="NAO_URGENTE")
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_audiencia = models.DateTimeField(null=True, blank=True)
    advogado_responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.numero_processo