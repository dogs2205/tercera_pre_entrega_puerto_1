"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Granja.views import index, mostrar_oveja,v_animal,v_alimento,v_contacto,agregar_post_animal,agregar_post_alimento,agregar_post_contacto, buscar_post

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    #path('animal/', mostrar_animal, name="animal"),
    #path('alimento/', mostrar_alimento, name="alimento"),
    #path('contacto/', mostrar_contacto, name="contacto"),
    path('oveja/', mostrar_oveja, name="oveja"),
    path('animal/',v_animal, name="animal"),
    path('alimento/', v_alimento, name="alimento"),
    path('contacto/', v_contacto, name="contacto"),
    path('animal/agregar',agregar_post_animal, name="agregar_post"),
    path('alimento/agregar',agregar_post_alimento, name="agregar_alimento"),
    path('contacto/agregar',agregar_post_contacto, name="agregar_contacto"),
    path('mis-posts/buscar', buscar_post, name="buscar-post"),

    
    
]
