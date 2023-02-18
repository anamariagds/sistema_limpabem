from django.db import models

class Atendente(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    senha = models.CharField(max_length=30)
   
    def __str__(self):
        return f'{self.nome}'

class Helper(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField()
   
    def __str__(self):
        return f'{self.nome}'
