from django.db import models

class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    data_lançamento = models.DateField(auto_now=True)
    data_efetivacao = models.DateField()
    categoria = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
    


class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    data_lançamento = models.DateField(auto_now=True)
    data_efetivacao = models.DateField()
    categoria = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descricao