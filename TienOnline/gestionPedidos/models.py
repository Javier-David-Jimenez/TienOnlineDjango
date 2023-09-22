from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    #Hacemos que no sea un campo obligatorio con el blank=True y el null = True
    #Como hemos modificado una clase tenemos que migrar... makemigrations y migrate
    email=models.EmailField(blank=True, null=True)
    tfno=models.CharField(max_length=9)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion= models.CharField(max_length=20)
    precio=models.IntegerField()
    
    def __str__(self): #Usamos funcion __str__ para cque nos devuelva un string
        return 'El nombre es %s la sección es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)
    #Esta funcion tambien se vera reflejada en el panel de control
"""cada vez que hacemos un cambio en el modelo debemos de volver a hacer las migracionessalimos de shell con -- exit() -- (si estamos en el) 
        y  migramos  python manage.py makemigrations  y despues  python manage.py migrate   despues python manage.py shell para volver al shell
       en shell Importamos la clase Articulos  from gestionPedidos.models import Articulos y despues usamos la clase Articulos.objects.filter(seccion'deportes')
"""

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
