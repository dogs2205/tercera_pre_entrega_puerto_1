from django.shortcuts import render

def index(request):
    return render(request, "Granja/index.html")

# Create your views here.
