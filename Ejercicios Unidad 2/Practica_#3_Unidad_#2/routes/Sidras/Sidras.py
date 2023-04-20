from flask import Blueprint, request,jsonify
from models import Sidras
from app import db

appSidras = Blueprint('appSidras',__name__,template_folder="templates")

@appSidras.route('/Sidras/agregar',methods={'POST'})
def agregarSidras():
    try:
        json = request.get_json()
        sidras = Sidras()
        sidras.Nombre = json['Nombre']
        sidras.Precio = json['Precio']
        db.session.add(sidras)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Sidras agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appSidras.route('/Sidras/editar',methods={"POST"})
def editarSidras():
    try:
        json = request.get_json()
        sidras = sidras.query.get_or_404(json['id'])
        sidras.Nombre = json['Nombre']
        sidras.Precio = json['Precio']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Sidras modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appSidras.route('/Sidras/eliminar',methods={"POST"})
def eliminarSidras():
    try:
        json = request.get_json()
        sidras = sidras.query.get_or_404(json['id'])
        db.session.delete(sidras)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Sidras eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appSidras.route('/Sidras/obtener',methods={"GET"})
def obtenerSidrass():
    sidras = sidras.query.all()
    listaSidrass=[]
    for p in sidras:
        sidras = {}
        sidras["Nombre"] = p.nombre
        sidras["Precio"] = p.precio
        listaSidrass.append(sidras)
    return jsonify({'Sidras':listaSidrass})