from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from models import Vinos
from forms import VinoForm
from app import db

appVinos = Blueprint('appVinos',__name__,template_folder='templates')

@appVinos.route('/indexd')
def inicio():
    vinos = vinos.query.all()
    totalVinoss = vinos.query.count()
    return render_template('indexd.html',vinos = vinos, totalVinoss = totalVinoss)

@appVinos.route('/agregard', methods=["GET","POST"])
def agregar():
    vinos = Vinos()
    vinosForm = VinoForm(obj=vinos)
    if request.method == "POST":
        if vinosForm.validate_on_submit():
            vinosForm.populate_obj(vinos)
            db.session.add(vinos)
            db.session.commit()
            return redirect(url_for('appVinos.inicio'))
    return render_template('agregard.html',forma=vinosForm)

@appVinos.route('/editard/<int:id>', methods=["GET","POST"])
def editar(id):
    vinos = vinos.query.get_or_404(id)
    vinosForm = VinoForm(obj=vinos)
    if request.method == "POST":
        if vinosForm.validate_on_submit():
            vinosForm.populate_obj(vinos)
            db.session.add(vinos)
            db.session.commit()
            return redirect(url_for('appVinos.inicio'))
    return render_template('editard.html',forma=vinosForm)


@appVinos.route('/detalled/<int:id>')
def detalle(id):
    vinos = vinos.query.get_or_404(id)
    return render_template('detalled.html',vinos = vinos)

@appVinos.route('/eliminard/<int:id>')
def eliminar(id):
    vinos = vinos.query.get_or_404(id)
    db.session.delete(vinos)
    db.session.commit()
    return redirect(url_for('appVinos.inicio'))

# -----------------------------------------------------------------------------------------------------------------------------------------


appVinos2 = Blueprint('appVinos2',__name__,template_folder="templates")

@appVinos2.route('/Vinos/agregar',methods={'POST'})
def agregarCheetos():
    try:
        json = request.get_json()
        vinos = Vinos()
        vinos.Nombre = json['Nombre']
        vinos.Precio = json['Precio']
        vinos.Marca = json['Marca']
        db.session.add(vinos)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Vinos agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appVinos2.route('/Vinos/editar',methods={"POST"})
def editarVinos():
    try:
        json = request.get_json()
        vinos = vinos.query.get_or_404(json['id'])
        vinos.Nombre = json['Nombre']
        vinos.Precio = json['Precio']
        vinos.Marca = json['Marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Vinos modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appVinos2.route('/Vinos/eliminar',methods={"POST"})
def eliminarVinos():
    try:
        json = request.get_json()
        vinos = vinos.query.get_or_404(json['id'])
        db.session.delete(vinos)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Vinos eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appVinos2.route('/Vinos/obtener',methods={"GET"})
def obtenerVinos():
    vinos = vinos.query.all()
    listaVinos=[]
    for p in vinos:
        vinos = {}
        vinos["Nombre"] = p.Nombre
        vinos["Precio"] = p.Precio
        vinos["Marca"] = p.Marca
        listaVinos.append(vinos)
    return jsonify({'Vinos':listaVinos})

    