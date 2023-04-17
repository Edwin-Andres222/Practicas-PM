from django.shortcuts import get_object_or_404, redirect, render
from Comentario.forms import ComentarioForm
from Comentario.models import Comentario
# Create your views here.
def detalleComentario(req, id) :
    comentario = get_object_or_404(Comentario, pk = id);
    return render(req, 'detalleCom.html', {'comentario': comentario});

def nuevoComentario(req) :
    if req.method == "POST":
        formaComentario = ComentarioForm(req.POST);

        if formaComentario.is_valid():
            formaComentario.save();
            return redirect('comentarioList');
    else:
        formaComentario = ComentarioForm();
        return render(req, 'agregarCom.html', {'formaComentario': formaComentario})

def editarComentario(req, id):
    comentario = get_object_or_404(Comentario, pk = id);
    if req.method == "POST":
        formaComentario = ComentarioForm(req.POST, instance = comentario);

        if formaComentario.is_valid():
            formaComentario.save();
            return redirect('comentarioList');
    else:
        formaComentario = ComentarioForm(instance = comentario);
        return render(req, 'editarCom.html', {'formaComentario': formaComentario})

def eliminarComentario(req, id):
    comentario = get_object_or_404(Comentario, pk = id);
    if comentario:
        comentario.delete();
        return redirect('comentarioList');