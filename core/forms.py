from django.forms import ModelForm
from .models import Tipo, Area, Publico, Campus


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