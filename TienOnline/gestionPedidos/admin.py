from django.contrib import admin

#ahora añadiremos las tablas de clientes articulos y pedidos al panel de administracion
from gestionPedidos.models import Clientes, Articulos, Pedidos


#creamos esta clase para que coja los datos que queremos de lod clientes en el panel de control
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno")
    search_fields=("nombre", "tfno")
#con el search_fields añadimos un buscador en este caso de los campos nombre y tfno
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)

