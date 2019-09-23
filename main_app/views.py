from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html', {'autos' : autos})

class Auto:
    def __init__(self, nombre, modelo, precio, color, km):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.km = km

autos = [
    Auto("VW Jetta", 2018, 145000, "Rojo",1300),
    Auto("Futura", 1955, 0, "Aqua",63000),
    Auto("Seat", 2002, 110000, "Azul",102500),
    #Auto("Ford ", 1999, 34000, "Negro",142000),
    Auto("Batmobile - Animated Series", 1992, 0, "Negro con parrila gris", 92000 ),
    Auto("Batmobile - 66'", 1966, 0, "Negro con delineado rojo", 66000 ),
    Auto("Batmobile - Tim Burton", 1989, 0, "Negro", 89000 ),
    Auto("Batmobile - Joel Schumacher", 1997, 0, "Negro", 97000 ),
    Auto("Batmobile - Tumbler", 2005, 0, "Negro", 25000 ),
    Auto("Batmobile - DCU", 2016, 0, "Negro", 16000 ),

]