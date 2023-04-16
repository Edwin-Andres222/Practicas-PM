from flask import Blueprint, request,jsonify
from models import Sidras
from app import db

appSidras = Blueprint('appSidras',__name__,template_folder="templates")

@appSidras.route('/Sidras/agregar',methods={'POST'})
def agregarSidras():
    try:
        json = request.get_json()
        Sidras = Sidras()
        Sidras.Nombre = json['Nombre']
        Sidras.Precio = json['Precio']
        db.session.add(Sidras)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Sidras agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appSidras.route('/Sidras/editar',methods={"POST"})
def editarSidras():
    try:
        json = request.get_json()
        Sidras = Sidras.query.get_or_404(json['id'])
        Sidras.Nombre = json['Nombre']
        Sidras.Precio = json['Precio']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Sidras modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appSidras.route('/Sidras/eliminar',methods={"POST"})
def eliminarSidras():
    try:
        json = request.get_json()
        Sidras = Sidras.query.get_or_404(json['id'])
        db.session.delete(Sidras)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Sidras eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appSidras.route('/Sidras/obtener',methods={"GET"})
def obtenerSidrass():
    Sidrass = Sidras.query.all()
    listaSidrass=[]
    for p in Sidrass:
        Sidras = {}
        Sidras["Nombre"] = p.nombre
        Sidras["Precio"] = p.precio
        listaSidrass.append(Sidras)
    return jsonify({'Sidras':listaSidrass})