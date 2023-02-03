from django.shortcuts import render, redirect, HttpResponse
from .models import Oportunidade, Tipo, Area, Publico, Campus,Usuario
from .forms import TipoForm, AreaForm, PublicoForm, CampusForm, UsuarioCreationForm, OportunidadeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

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




def editar_tipo(request, id):
    tipo = Tipo.objects.get(pk=id)
    form = TipoForm(request.POST or None, instance=tipo)
    
    if form.is_valid():
        form.save()
        return redirect('listar_tipo')
    
    contexto = {
        'form_tipo': form
    }
        
    return render(request, 'tipo_cadastrar.html', contexto)

def editar_area(request, id):
    areas = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=areas)
    
    if form.is_valid():
        form.save()
        return redirect('listar_area')
    
    contexto = {
        'form_area': form
    }
    return render(request, 'area_cadastrar.html', contexto)

def editar_publico(request, id):
    publico = Publico.objects.get(pk=id)
    form = PublicoForm(request.POST or None, instance=publico)
    
    if form.is_valid():
        form.save()
        return redirect('listar_publico')
    
    contexto = {
        'form_publico': form
    }
        
    return render(request, 'publico_cadastrar.html', contexto)

def editar_campus(request, id):
    campus = Campus.objects.get(pk=id)    
    form = CampusForm(request.POST or None, instance=campus)
    
    if form.is_valid():
        form.save()
        return redirect('listar_campus')
    
    contexto = {
        'form_campus': form
    }
        
    return render(request, 'campus_cadastrar.html', contexto)


def remover_tipo(request, id):
    tipo = Tipo.objects.get(pk=id)
    tipo.delete()
    return redirect('listar_tipo')

def remover_area(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('listar_area')

def remover_publico(request, id):
    publico = Publico.objects.get(pk=id)
    publico.delete()
    return redirect('listar_publico')

def remover_campus(request, id):
    campus = Campus.objects.get(pk=id)
    campus.delete()
    return redirect('listar_campus')


def home(request):
    oportunidades = Oportunidade.objects.all()
    contexto = {
    'todos_oportunidades': oportunidades
    }    
    return render(request, 'index.html', contexto)

@login_required
def perfil(request):
    return render(request, 'perfil.html')


def desconectar(request):
    logout(request)
    return redirect('home')



def registro(request):
    form = UsuarioCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'registro.html', contexto)

@login_required
def dados(request, id):
    user = Usuario.objects.get(pk=id)
    form = UsuarioCreationForm(request.POST or None, instance=user)
    if form.is_valid():
       form.save()
       return redirect('perfil')
    contexto = {
        'form': form
    }
    return render(request, 'registro.html', contexto)


def cadastrar_oportunidade(request):
   
    form = OportunidadeForm(request.POST or None, request.FILES or None, instance=oportunidade),  
    if form.is_valid():
       form.save()
       return redirect('listar_oportunidade')
    
    contexto = {
        'form': form
    }
    return render(request, 'oportunidade_cadastrar.html', contexto)



def listar_oportunidade(request):
    oportunidades = Oportunidade.objects.all()
    contexto = {
        'todos_oportunidades': oportunidades
    }
    return render(request, 'oportunidades.html', contexto)


def editar_oportunidade(request, id):
    oportunidades = Oportunidade.objects.get(pk=id)    
    form = OportunidadeForm(request.POST or None, request.FILES or None, instance=oportunidades)
    form = OportunidadeForm(request.POST or None, instance=oportunidades)
    
    if form.is_valid():
        form.save()
        return redirect('listar_oportunidade')
    
    contexto = {
        'form': form
    }
        
    return render(request, 'oportunidade_cadastrar.html', contexto)

def remover_oportunidade(request, id):
    oportunidades = Oportunidade.objects.get(pk=id)
    oportunidades.delete()
    return redirect('listar_oportunidade')


