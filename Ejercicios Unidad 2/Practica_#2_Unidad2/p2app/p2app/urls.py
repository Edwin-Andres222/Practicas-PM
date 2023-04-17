"""
URL configuration for p2app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Usuario.views import detalleUsuario, nuevoUsuario, eliminarUsuario, editarUsuario
from webapp.views import comentarioView, usuarioView, mainView, categoriaView, productoView, proveedorView, ventaView
from Categoria.views import detalleCategoria, nuevoCategoria, eliminarCategoria, editarCategoria
from Producto.views import detalleProducto, nuevoProducto, eliminarProducto, editarProducto
from Proveedor.views import detalleProveedor, nuevoProveedor, editarProveedor, eliminarProveedor
from Venta.views import detalleVenta, nuevoVenta, eliminarVenta, editarVenta 
from Comentario.views import detalleComentario, nuevoComentario, editarComentario, eliminarComentario
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainView, name='index'),

    path('lista_usuarios', usuarioView, name='usuarioList'),
    path('detalle_usuario/<int:id>', detalleUsuario),
    path('nuevo_usuario', nuevoUsuario),
    path('editar_usuario/<int:id>', editarUsuario),
    path('eliminar_usuario/<int:id>', eliminarUsuario),
    
    path('lista_categorias', categoriaView, name='categoriaList'),
    path('detalle_categoria/<int:id>', detalleCategoria),
    path('nuevo_categoria', nuevoCategoria),
    path('editar_categoria/<int:id>', editarCategoria),
    path('eliminar_categoria/<int:id>', eliminarCategoria),

    path('lista_productos', productoView, name='productoList'),
    path('detalle_producto/<int:id>', detalleProducto),
    path('nuevo_producto', nuevoProducto),
    path('editar_producto/<int:id>', editarProducto),
    path('eliminar_producto/<int:id>', eliminarProducto),

    path('lista_proveedores', proveedorView, name='proveedorList'),
    path('detalle_proveedor/<int:id>', detalleProveedor),
    path('nuevo_proveedor', nuevoProveedor),
    path('editar_proveedor/<int:id>', editarProveedor),
    path('eliminar_proveedor/<int:id>', eliminarProveedor),

    path('lista_ventas', ventaView, name='ventaList'),
    path('detalle_venta/<int:id>', detalleVenta),
    path('nuevo_venta', nuevoVenta),
    path('editar_venta/<int:id>', editarVenta),
    path('eliminar_venta/<int:id>', eliminarVenta),

    path('lista_comentarios', comentarioView, name='comentarioList'),
    path('detalle_comentario/<int:id>', detalleComentario),
    path('nuevo_comentario', nuevoComentario),
    path('editar_comentario/<int:id>', editarComentario),
    path('eliminar_comentario/<int:id>', eliminarComentario),
]
