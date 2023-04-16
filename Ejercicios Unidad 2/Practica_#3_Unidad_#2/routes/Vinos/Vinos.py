from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from models import Vinos
from forms import VinoForm
from app import db

appVinos = Blueprint('appVinos',__name__,template_folder='templates')

@appVinos.route('/indexd')
def inicio():
    Vinos = Vinos.query.all()
    totalVinoss = Vinos.query.count()
    return render_template('indexd.html',Vinos = Vinos, totalVinoss = totalVinoss)

@appVinos.route('/agregard', methods=["GET","POST"])
def agregar():
    Vinos = Vinos()
    VinosForm = VinoForm(obj=Vinos)
    if request.method == "POST":
        if VinosForm.validate_on_submit():
            VinosForm.populate_obj(Vinos)
            db.session.add(Vinos)
            db.session.commit()
            return redirect(url_for('appVinos.inicio'))
    return render_template('agregard.html',forma=VinosForm)

@appVinos.route('/editard/<int:id>', methods=["GET","POST"])
def editar(id):
    Vinos = Vinos.query.get_or_404(id)
    VinosForm = VinoForm(obj=Vinos)
    if request.method == "POST":
        if VinosForm.validate_on_submit():
            VinosForm.populate_obj(Vinos)
            db.session.add(Vinos)
            db.session.commit()
            return redirect(url_for('appVinos.inicio'))
    return render_template('editard.html',forma=VinosForm)


@appVinos.route('/detalled/<int:id>')
def detalle(id):
    dulce = Vinos.query.get_or_404(id)
    return render_template('detalled.html',dulce = dulce)

@appVinos.route('/eliminard/<int:id>')
def eliminar(id):
    Vinos = Vinos.query.get_or_404(id)
    db.session.delete(Vinos)
    db.session.commit()
    return redirect(url_for('appVinos.inicio'))

# -----------------------------------------------------------------------------------------------------------------------------------------


appVinos2 = Blueprint('appVinos2',__name__,template_folder="templates")

@appVinos2.route('/Vinos/agregar',methods={'POST'})
def agregarCheetos():
    try:
        json = request.get_json()
        Vinos = Vinos()
        Vinos.Nombre = json['Nombre']
        Vinos.Precio = json['Precio']
        Vinos.Marca = json['Marca']
        db.session.add(Vinos)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Vinos agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appVinos2.route('/Vinos/editar',methods={"POST"})
def editarVinos():
    try:
        json = request.get_json()
        Vinos = Vinos.query.get_or_404(json['id'])
        Vinos.Nombre = json['Nombre']
        Vinos.Precio = json['Precio']
        Vinos.Marca = json['Marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Vinos modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appVinos2.route('/Vinos/eliminar',methods={"POST"})
def eliminarVinos():
    try:
        json = request.get_json()
        Vinos = Vinos.query.get_or_404(json['id'])
        db.session.delete(Vinos)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Vinos eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appVinos2.route('/Vinos/obtener',methods={"GET"})
def obtenerVinos():
    Vinos = Vinos.query.all()
    listaVinos=[]
    for p in Vinos:
        Vinos = {}
        Vinos["Nombre"] = p.Nombre
        Vinos["Precio"] = p.Precio
        Vinos["Marca"] = p.Marca
        listaVinos.append(Vinos)
    return jsonify({'Vinos':listaVinos})

    