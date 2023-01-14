from django.shortcuts import render, redirect
from .models import Tipo, Area, Publico, Campus
from .forms import TipoForm, AreaForm, PublicoForm, CampusForm


def listar_tipo(request):
    tipos = Tipo.objects.all()
    contexto = {
        'todos_tipo': tipos
    }
    return render(request, 'tipo.html', contexto)

def listar_area(request):
    areas = Area.objects.all()
    contexto = {
        'todos_area': areas
    }
    return render(request, 'area.html', contexto)

def listar_publico(request):
    publico = Publico.objects.all()
    contexto = {
        'todos_publico': publico
    }
    return render(request, 'publico.html', contexto)

def listar_campus(request):
    campus = Campus.objects.all()
    contexto = {
        'todos_campus': campus
    }
    return render(request, 'campus.html', contexto)



def cadastrar_tipo(request):
    form = TipoForm(request.POST or None)  
    if form.is_valid():
       form.save()
       return redirect('listar_tipo')
    
    contexto = {
        'form_tipo': form
    }
    return render(request, 'tipo_cadastrar.html', contexto)

def cadastrar_area(request):
    form = AreaForm(request.POST or None)

    if form.is_valid():
       form.save()
       return redirect('listar_area')    

    contexto = {
        'form_area': form
    }
    return render(request, 'area_cadastrar.html', contexto)

def cadastrar_publico(request):
    form = PublicoForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('listar_publico')    
    
    contexto = {
        'form_publico': form
    }
    return render(request, 'publico_cadastrar.html', contexto)

def cadastrar_campus(request):
    form = CampusForm(request.POST or None)
  
    if form.is_valid():
       form.save()
       return redirect('listar_campus')

    contexto = {
        'form_campus': form
    }
    return render(request, 'campus_cadastrar.html', contexto)
