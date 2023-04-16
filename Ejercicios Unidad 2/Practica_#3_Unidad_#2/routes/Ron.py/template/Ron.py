from flask import Blueprint, request, render_template, redirect, url_for
from models import Ron
from forms import RonForm
from app import db

appRon = Blueprint('appRon',__name__,template_folder='templates')

@appRon.route('/index')
def inicio():
    Rons = Ron.query.all()
    totalRons = Ron.query.count()
    return render_template('index.html',Rons = Rons, totalRons = totalRons)

@appRon.route('/agregar', methods=["GET","POST"])
def agregar():
    Ron = Ron()
    RonForm = RonForm(obj=Ron)
    if request.method == "POST":
        if RonForm.validate_on_submit():
            RonForm.populate_obj(Ron)
            db.session.add(Ron)
            db.session.commit()
            return redirect(url_for('appRon.inicio'))
    return render_template('agregar.html',forma=RonForm)

@appRon.route('/editar/<int:id>', methods=["GET","POST"])
def editar(id):
    Ron = Ron.query.get_or_404(id)
    RonForm = RonForm(obj=Ron)
    if request.method == "POST":
        if RonForm.validate_on_submit():
            RonForm.populate_obj(Ron)
            db.session.add(Ron)
            db.session.commit()
            return redirect(url_for('appRon.inicio'))
    return render_template('editar.html',forma=RonForm)


@appRon.route('/detalle/<int:id>')
def detalle(id):
    Ron = Ron.query.get_or_404(id)
    return render_template('detalle.html',Ron = Ron)

@appRon.route('/eliminar/<int:id>')
def eliminar(id):
    Ron = Ron.query.get_or_404(id)
    db.session.delete(Ron)
    db.session.commit()
    return redirect(url_for('appRon.inicio'))


    