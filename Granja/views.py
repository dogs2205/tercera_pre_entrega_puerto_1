from django.shortcuts import render
from Granja.models import Post,Alimento,Contacto
from Granja.forms import PostForm

def index(request):
    return render(request, "Granja/index.html")

#def mostrar_animal(request):
 #   posts = Post.objects.all()
  #  return render(request, "Granja/vista_animal.html", {"posts":posts})

def v_animal(request):
    context={
        "form":PostForm(),
    }
    return render(request, "Granja/admin.html",context)


def mostrar_alimento(request):
    alimento=Alimento.objects.all()
    return render(request, "Granja/vista_alimento.html", {"alimento":alimento})

def mostrar_contacto(request):
    contacto=Contacto.objects.all()
    return render(request, "Granja/vista_contacto.html",{"contacto":contacto})

def mostrar_oveja(request):
    return render(request, "Granja/vista_oveja.html")

def view_animal(request):
    return render(request,"Granja/admin_post.html")



# Create your views here.
