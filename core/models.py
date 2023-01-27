from django.db import models

class Tipo(models.Model):
    nome = models.CharField('nome', max_length=100)
    
class Area(models.Model):
    nome = models.CharField('nome', max_length=100)
    
class Publico(models.Model):
    nome = models.CharField('nome', max_length=100)
    
class Campus(models.Model):
    nome = models.CharField('nome', max_length=100)

   
class Usuario(models.Model):
    usuario1 = models.CharField('usuario1', max_length=100)
    senha1 = models.CharField('senha1', max_length=100)
    senha2 = models.CharField('senha2', max_length=100)
    cpf = models.CharField('cpf', max_length=11)
    email = models.CharField('email', max_length=100)
    phone = models.CharField('phone', max_length=9)
    date = models.CharField('date', max_length=8)
    idade = models.CharField('idade', max_length=2)

    USERNAME_FIELD = 'cpf'

class Oportunidade(models.Model):
    titulo = models.CharField('nome', max_length=100)
    anexo = models.CharField('anexo', max_length=100)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)

