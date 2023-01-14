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
from core.views import listar_tipo, listar_area, listar_publico, listar_campus, cadastrar_tipo, cadastrar_area, cadastrar_publico, cadastrar_campus


urlpatterns = [
    path('tipo/', listar_tipo, name='listar_tipo'),
    path('area/', listar_area, name='listar_area'),
    path('publico/', listar_publico, name='listar_publico'),
    path('campus/', listar_campus, name='listar_campus'),
    
    path('tipo_cadastrar/', cadastrar_tipo, name='cadastrar_tipo'),
    path('area_cadastrar/', cadastrar_area, name='cadastrar_area'),
    path('publico_cadastrar/', cadastrar_publico, name='cadastrar_publico'),
    path('campus_cadastrar/', cadastrar_campus, name='cadastrar_campus'),
    
    path('admin/', admin.site.urls),
]

