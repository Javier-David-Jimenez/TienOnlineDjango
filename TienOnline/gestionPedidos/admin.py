from django.contrib import admin

#ahora añadiremos las tablas de clientes articulos y pedidos al panel de administracion
from gestionPedidos.models import Clientes, Articulos, Pedidos
admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)