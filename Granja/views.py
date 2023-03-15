from django.shortcuts import render
from Granja.models import Post,Alimento,Contacto
from Granja.forms import PostForm,AlimentoForm,ContactoForm

def index(request):
    return render(request, "Granja/index.html")

#def mostrar_animal(request):
 #   posts = Post.objects.all()
  #  return render(request, "Granja/vista_animal.html", {"posts":posts})

def v_animal(request):
    context={
        "post": Post.objects.all(),
        "form": PostForm(),
    }
    return render(request, "Granja/admin.html",context)

def agregar_post_animal(request):
    post_form=PostForm(request.POST)
    post_form.save()
    context={
        "posts": Post.objects.all(),
        "form":PostForm()

    }
    return render(request, "Granja/admin.html", context)

def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = { "posts": Post.objects.filter(nombre_animal=criterio).all()}
    
    return render(request, "Granja/admin.html", context)
# Create your views here.


#def mostrar_alimento(request):
 #   alimento=Alimento.objects.all()
  #  return render(request, "Granja/vista_alimento.html", {"alimento":alimento})

def v_alimento(request):
    context={
        "post": Alimento.objects.all(),
        "form":AlimentoForm(),
    }
    return render(request, "Granja/admin_alimento.html",context)

def agregar_post_alimento(request):
    alimento_form=AlimentoForm(request.POST)
    alimento_form.save()
    context={
        "post": Alimento.objects.all(),
        "form":AlimentoForm(),

    }
    return render(request, "Granja/admin_alimento.html", context)


#def mostrar_contacto(request):
 #   contacto=Contacto.objects.all()
  #  return render(request, "Granja/vista_contacto.html",{"contacto":contacto})

def v_contacto(request):
    context={
        "post": Contacto.objects.all(),
        "form":ContactoForm(),
    }
    return render(request, "Granja/admin_contacto.html",context)

def agregar_post_contacto(request):
    contacto_form=ContactoForm(request.POST)
    contacto_form.save()
    context={
        "post": Contacto.objects.all(),
        "form":AlimentoForm(),
    }
    return render(request, "Granja/admin_contacto.html", context)

def mostrar_oveja(request):
    return render(request, "Granja/vista_oveja.html")







# Create your views here.
