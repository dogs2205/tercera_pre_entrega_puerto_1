from django.shortcuts import render
from Granja.models import Post

def index(request):
    return render(request, "Granja/index.html")

def mostrar_perro(request):
    posts = Post.objects.all()
    return render(request, "Granja/vista_perro.html", {"posts":posts})

def mostrar_vaca(request):
    return render(request, "Granja/vista_vaca.html")

def mostrar_caballo(request):
    return render(request, "Granja/vista_caballo.html")

def mostrar_oveja(request):
    return render(request, "Granja/vista_oveja.html")



# Create your views here.
