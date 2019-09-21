from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    #return render(request, 'index.html')
    #return HttpResponse("<h1>Bienvenido a Automart</h1>")

    nombre = "VW Jetta"
    modelo = 2018
    precio = 145000
    color = "Rojo"

    context = {'auto_nombre' : nombre, 'auto_modelo' : modelo, 'auto_precio' : precio, 'auto_color' : color}

    return render(request, 'index.html', context)