from django.db import models
from django.utils import timezone
from funcionarios.models import Atendente, Helper

class Servico(models.Model):
   servico = models.CharField(max_length=30)
   descricao = models.TextField()
   preco = models.DecimalField(max_digits=10, decimal_places=2)
   
   def __str__(self):
        return f'{self.servico}'

class Atendimento(models.Model):
    choiches_status = (('P', 'Pendente'),
                       ('R', 'Realizado'),
                       ('C', 'Cancelado'))
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_agendada = models.DateTimeField()
    status = models.CharField(max_length=1, choices=choiches_status, default='P')
    
    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE)
    helper =  models.ForeignKey(Helper, on_delete=models.CASCADE)

    nome_cliente = models.CharField(max_length=100)
    fone_cliente = models.CharField(max_length=30)
    rua = models.CharField(max_length=30)
    casa =models.CharField(max_length=10)
    bairro = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.nome_cliente} | {self.servico}'
    