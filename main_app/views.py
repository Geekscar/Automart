from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html', {'autos' : autos})

class Auto:
    def __init__(self, nombre, modelo, precio, color, km, img_url):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.km = km
        self.img_url = img_url

#image = "https://i.ytimg.com/vi/neBuTKGYDD4/maxresdefault.jpg" 

autos = [
    Auto("VW Jetta", 2018, 145000, "Rojo",1300, "https://i.ytimg.com/vi/neBuTKGYDD4/maxresdefault.jpg"),
    Auto("Futura", 1955, 0, "Aqua",63000, "https://i.pinimg.com/originals/d1/d3/8d/d1d38dbdfa218d39ef6c9fbe30a121ed.jpg"),
    Auto("Seat", 2002, 110000, "Azul",102500, "https://images.evisos.com.mx/2010/08/07/seat-ibiza-2002-azul-excelente-manejo-bonito-deportivo_b9570f3b_3.jpg"),
    #Auto("Ford ", 1999, 34000, "Negro",142000),
    Auto("Batmobile - Animated Series", 1992, 0, "Negro con parrila gris", 92000, "https://images-na.ssl-images-amazon.com/images/I/71f9GBZ9WXL._SX425_.jpg" ),
    Auto("Batmobile - 66'", 1966, 0, "Negro con delineado rojo", 66000, "https://i5.walmartimages.com/asr/53825e0d-26ed-4722-8019-4826d079ee4d_1.451376f6106161c3eb5d241f9d70bdae.jpeg"),
    Auto("Batmobile - Tim Burton", 1989, 0, "Negro", 89000, "https://i.pinimg.com/originals/ba/28/4d/ba284d8e8971964092f7e724a86dca29.jpg" ),
    Auto("Batmobile - Joel Schumacher", 1997, 0, "Negro", 97000, "https://vignette.wikia.nocookie.net/starcars/images/e/ef/Batmobile_batman_forever_movie_1995_val_kilmer_.jpg/revision/latest?cb=20120827203807" ),
    Auto("Batmobile - Tumbler", 2005, 0, "Negro", 25000, "https://vignette.wikia.nocookie.net/batman/images/5/57/Thedarkknight17po4.jpg/revision/latest?cb=20120113141554" ),
    Auto("Batmobile - DCU", 2016, 0, "Negro", 16000, "https://i0.wp.com/www.moviesinfocus.com/wp-content/uploads/2015/09/batmobile-batman-vs-superman-1.jpg" ),

]