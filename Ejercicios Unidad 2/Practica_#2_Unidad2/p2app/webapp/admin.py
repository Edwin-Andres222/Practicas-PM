# Register your models here.
from django.contrib import admin
from Usuario.models import Usuario
from Categoria.models import Categoria
from Producto.models import Producto
from Proveedor.models import Proveedor
from Venta.models import Venta
from Comentario.models import Comentario

admin.site.register(Usuario);
admin.site.register(Categoria);
admin.site.register(Producto);
admin.site.register(Proveedor);
admin.site.register(Venta);
admin.site.register(Comentario);