from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    
    #Con este if hacemos que si no introduce nada y le da a buscar, no envie la pregunta a la BBDD
    if request.GET["prd"]:
        #Esta variable toma prd y la une a Articulo buscado
        #mensaje="Artículo buscado: %r" %request.GET["prd"]
        
        #producto coge el "prd" que han introducido en buscar
        producto = request.GET["prd"]
        
        #la funcion nombre__icontain funciona como un filter de SQL  like nombre="producto"
        articulos = Articulos.objects.filter(nombre__icontains=producto)
        
        return render(request, "resultados_busqueda.html", {"articulos":articulos, "query": producto})
    else:
        mensaje = "No has introducido nada"
    return HttpResponse(mensaje)