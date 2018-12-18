from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class Acao(models.Model):
    sigla = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="acoes")
    dt_inicio = models.DateField()

    def __str__(self):
        return self.sigla

class Cotacao(models.Model):
    dt_valor = models.DateField()
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, related_name="cotacoes")
    valor = models.CharField(max_length=10)
