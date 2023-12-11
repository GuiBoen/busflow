from django.db import models
from django.conf import settings

objects = models.Manager()
class horario32(models.Model):
    horario = models.TimeField()

# Create your models here.
class linhas(models.Model):
    nome = models.CharField(max_length=255)
    List_id_pontos = models.CharField(max_length=255)
    numero = models.IntegerField()

    def __str__(self):
        return f'{self.nome} - {self.numero}'

class onibus(models.Model):
    last_time = models.TimeField(null=True)
    id_last_ponto = models.ForeignKey('pontos', on_delete=models.CASCADE, null=True)
    lotacao = models.IntegerField(default=0)
    id_linha = models.ForeignKey(linhas, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_linha}'

class pontos(models.Model):
    nome = models.CharField(max_length=255)
    lotacao = models.IntegerField(default=0)
    id_onibus = models.ForeignKey(onibus, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.nome} ({self.lotacao})'

class usuario(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    is_adm = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    id_ponto = models.ForeignKey(pontos, on_delete=models.CASCADE, null=True)
    id_onibus = models.ForeignKey(onibus, on_delete=models.CASCADE, null=True)
