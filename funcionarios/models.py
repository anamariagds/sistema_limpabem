from django.db import models

class Funcionario(models.Model):
    choices_status = (
        ('G', 'Gerente'),
        ('A', 'Atendente'),
        ('H', 'Helper')
    )
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    senha = models.CharField(max_length=30)
    status = models.CharField(max_length=2, choices=choices_status, default='A')

    def __str__(self):
        return f'{self.nome} | {self.status}'
    
