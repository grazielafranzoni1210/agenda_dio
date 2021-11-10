from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')  # pode vir o campo vazio e também pode ser nulo
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da criação') # campo automático, sem o usuário precisar alterando
    usuario = models.ForeignKey(User, models.CASCADE) # se o usuário for excluído da app, excluí também todos os eventos dele


    class Meta:
        db_table = "evento"

    def __str__(self):
        return self.titulo

