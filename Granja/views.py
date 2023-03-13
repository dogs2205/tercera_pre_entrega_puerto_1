from django.shortcuts import render
from Granja.models import Post,Alimento

def index(request):
    return render(request, "Granja/index.html")

def mostrar_animal(request):
    posts = Post.objects.all()
    return render(request, "Granja/vista_animal.html", {"posts":posts})

def mostrar_alimento(request):
    alimento=Alimento.objects.all()
    return render(request, "Granja/vista_alimento.html", {"alimento":alimento})


def mostrar_contacto(request):
    return render(request, "Granja/vista_contacto.html")

def mostrar_oveja(request):
    return render(request, "Granja/vista_oveja.html")



# Create your views here.
