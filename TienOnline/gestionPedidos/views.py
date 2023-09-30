from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
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
        
        #anidamos otro if y con el metodo len comprobamos si es mayor de 25. haciendo la busqueda o dando un mensaje de "error"
        if len(producto)>25:
            mensaje = "Texto de busquea demasiado largo"
            
        else:
        #la funcion nombre__icontain funciona como un filter de SQL  like nombre="producto"
            articulos = Articulos.objects.filter(nombre__icontains=producto)
        
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query": producto})
    else:
        mensaje = "No has introducido nada"
    return HttpResponse(mensaje)


def contacto(request):
    if request.method=="POST":
        
        subject = request.POST["asunto"]
        message = request.POST["mensaje"]+ " "+request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["djangomaster2023@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
            
        return render(request, "gracias.html" )
    
    return render(request, "contacto.html")
#La primera vez leera el contacto.html y la segunada nos enviara a gracias.html.