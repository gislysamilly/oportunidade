from django import forms
from django.forms import ModelForm
from .models import Tipo, Area, Publico, Campus, Usuario, Oportunidade
from django.contrib.auth.forms import UserCreationForm


class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']
        widgets = {
            'tipo': forms.RadioSelect()
        }
         
class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['nome']
        widgets = {
            'tipo': forms.RadioSelect()
        }       
         
class PublicoForm(ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']
        widgets = {
            'tipo': forms.CheckboxSelectMultiple()
        }     

         
class CampusForm(ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']
        widgets = {
            'tipo': forms.RadioSelect()
        }     

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','cpf','email','matricula','setor','password1','password2']

class OportunidadeForm (ModelForm):
    class Meta:
        model = Oportunidade
        fields = ['titulo', 'anexo', 'area', 'campus', 'tipo', 'publicos']