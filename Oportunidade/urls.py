"""Oportunidade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import listar_oportunidade, listar_tipo, listar_area, listar_publico, listar_campus, listar_oportunidade
from core.views import cadastrar_tipo, cadastrar_area, cadastrar_publico, cadastrar_campus, cadastrar_oportunidade
from core.views import editar_tipo, editar_area, editar_publico, editar_campus, editar_oportunidade
from core.views import remover_tipo, remover_area, remover_publico, remover_campus, perfil, remover_oportunidade
from django.contrib.auth.views import LoginView, LogoutView
from core.views import home, registro

urlpatterns = [
    path('tipo/', listar_tipo, name='listar_tipo'),
    path('area/', listar_area, name='listar_area'),
    path('publico/', listar_publico, name='listar_publico'),
    path('campus/', listar_campus, name='listar_campus'),
    path('tipo_cadastrar/', cadastrar_tipo, name='cadastrar_tipo'),
    path('area_cadastrar/', cadastrar_area, name='cadastrar_area'),
    path('publico_cadastrar/', cadastrar_publico, name='cadastrar_publico'),
    path('campus_cadastrar/', cadastrar_campus, name='cadastrar_campus'),
    path('tipo_editar/<int:id>/', editar_tipo, name='editar_tipo'),
    path('area_editar/<int:id>/', editar_area, name='editar_area'),
    path('publico_editar/<int:id>/', editar_publico, name='editar_publico'),
    path('campus_editar/<int:id>/', editar_campus, name='editar_campus'),
    path('tipo_remover/<int:id>/', remover_tipo, name='remover_tipo'),
    path('area_remover/<int:id>/', remover_area, name='remover_area'),
    path('publico_remover/<int:id>/', remover_publico, name='remover_publico'),
    path('campus_remover/<int:id>/', remover_campus, name='remover_campus'),
    path('', home),
    path('perfil/', perfil, name='perfil'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('oportunidade_cadastrar/', cadastrar_oportunidade, name='cadastrar_oportunidade'),
    path('oportunidades/', listar_oportunidade, name='listar_oportunidade'),
    path('oportunidade_editar/<int:id>/', editar_oportunidade, name='editar_oportunidade'),
    path('oportunidade_remover/<int:id>/', remover_oportunidade, name='remover_oportunidade'),
    
    
    path('admin/', admin.site.urls),

    path('registro/', registro, name='registro'),
    
]

