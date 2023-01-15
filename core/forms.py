from django import forms
from django.forms import ModelForm
from .models import Tipo, Area, Publico, Campus, Usuario
from django.contrib.auth.forms import UserCreationForm


class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']
         
class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['nome']
         
class PublicoForm(ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']
         
class CampusForm(ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['usuario1','senha1','senha2','cpf','email','date','idade', 'phone']
