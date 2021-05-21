from django.contrib import admin

from .models import Localizacion, Producto, Categoria, Proveedor, Pedido, DetallePedido

# Register your models here.
admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
