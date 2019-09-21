from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html', {'autos' : autos})

class Auto:
    def __init__(self, nombre, modelo, precio, color):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.color = color

autos = [
    Auto("VW Jetta", 2018, 145000, "Rojo"),
    Auto("Futura", 1955, 0, "Aqua"),
    Auto("Seat", 2002, 110000, "Azul"),
    Auto("Ford ", 1999, 34000, "Negro")
]