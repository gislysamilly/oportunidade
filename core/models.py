from django.db import models

class Tipo(models.Model):
    nome = models.CharField('nome', max_length=100)
    
class Area(models.Model):
    nome = models.CharField('nome', max_length=100)
    
class Publico(models.Model):
    nome = models.CharField('nome', max_length=100)
    
class Campus(models.Model):
    nome = models.CharField('nome', max_length=100)