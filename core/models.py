from django.db import models
from django.contrib.auth.models import AbstractUser

class Tipo(models.Model):
    nome = models.CharField('nome', max_length=100)
    def __str__(self):
        return self.nome
    
class Area(models.Model):
    nome = models.CharField('nome', max_length=100)
    
    def __str__(self):
        return self.nome
    
class Publico(models.Model):
    nome = models.CharField('nome', max_length=100)
    def __str__(self):
        return self.nome
    
class Campus(models.Model):
    nome = models.CharField('nome', max_length=100)
    def __str__(self):
        return self.nome

   
class Usuario(AbstractUser):
    username = models.CharField('username', max_length=100)
    cpf = models.CharField('cpf', max_length=11, unique =True)
    email = models.CharField('email', max_length=100)
    matricula = models.CharField('matricula', max_length=100)
    setor = models.CharField('setor', max_length=100)

    USERNAME_FIELD = 'cpf'

class Oportunidade(models.Model):
    titulo = models.CharField('nome', max_length=100)
    anexo = models.ImageField("anexo", upload_to="oportunidades/", null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)
  
    


