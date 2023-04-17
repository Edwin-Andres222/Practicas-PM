# Create your views here.
from django.shortcuts import render
from Usuario.models import Usuario
from Categoria.models import Categoria
from Producto.models import Producto
from Proveedor.models import Proveedor
from Venta.models import Venta 
from Comentario.models import Comentario

def mainView(req):
    return render(req, 'index.html');

def usuarioView(req):
    usuarios = Usuario.objects.order_by('id');
    return render(req, 'usuariosList.html', {'usuarios':usuarios});

def categoriaView(req):
    categorias = Categoria.objects.order_by('id');
    return render(req, 'categoriasList.html', {'categorias':categorias});

def productoView(req):
    productos = Producto.objects.order_by('id');
    return render(req, 'productosList.html', {'productos':productos});

def proveedorView(req):
    proveedores = Proveedor.objects.order_by('id');
    return render(req, 'proveedoresList.html', {'proveedores':proveedores});

def ventaView(req):
    ventas = Venta.objects.order_by('id');
    return render(req, 'ventasList.html', {'ventas':ventas});

def comentarioView(req):
    comentarios = Comentario.objects.order_by('id');
    return render(req, 'comentariosList.html', {'comentarios':comentarios});