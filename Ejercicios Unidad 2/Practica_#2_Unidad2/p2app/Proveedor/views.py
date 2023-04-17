from django.shortcuts import get_object_or_404, redirect, render
from Proveedor.forms import ProveedorForm
from Proveedor.models import Proveedor

def detalleProveedor(req, id) :
    proveedor = get_object_or_404(Proveedor, pk = id);
    return render(req, 'detallePro.html', {'proveedor': proveedor});

def nuevoProveedor(req) :
    if req.method == "POST":
        formaProveedor = ProveedorForm(req.POST);

        if formaProveedor.is_valid():
            formaProveedor.save();
            return redirect('proveedorList');
    else:
        formaProveedor = ProveedorForm();
        return render(req, 'agregarPro.html', {'formaProveedor': formaProveedor})

def editarProveedor(req, id):
    proveedor = get_object_or_404(Proveedor, pk = id);
    if req.method == "POST":
        formaProveedor = ProveedorForm(req.POST, instance = proveedor);

        if formaProveedor.is_valid():
            formaProveedor.save();
            return redirect('proveedorList');
    else:
        formaProveedor = ProveedorForm(instance = proveedor);
        return render(req, 'editarPro.html', {'formaProveedor': formaProveedor})

def eliminarProveedor(req, id):
    proveedor = get_object_or_404(Proveedor, pk = id);
    if proveedor:
        proveedor.delete();
        return redirect('proveedorList');
