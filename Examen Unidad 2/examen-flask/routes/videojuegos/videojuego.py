from flask import Blueprint, request, jsonify,render_template,url_for,redirect
from models import VideoJuego
from forms import VideoJuegoForm
from app import db

## los blueprints ayudan a construir sub aplicaciones, como sub proyectos, se hace independiente
## lo unico que cambia seria la db y el modelo
appVideoJuego = Blueprint('appVideoJuego',__name__,template_folder="templates")



## Videojuegos
@appVideoJuego.route('/')
@appVideoJuego.route('/index')
@appVideoJuego.route('/minecraft')
def inicio():
    videoj = VideoJuego.query.all()
    totalDevideoj = VideoJuego.query.count()
    ##app.logger.debug(f'Listado de videojuegos {videoj}')
    return render_template('index.html', videoj = videoj, totalDevideoj = totalDevideoj)

    

@appVideoJuego.route('/agregar', methods = ["GET","POST"])
def agregar(): 
    videoj = VideoJuego()
    videojForm = VideoJuegoForm(obj=videoj)
    if request.method == "POST":
        if videojForm.validate_on_submit():
            videojForm.populate_obj(videoj)
            db.session.add(videoj)
            db.session.commit()
            return redirect(url_for('appVideoJuego.inicio'))
    return render_template('agregar.html', forma = videojForm)

@appVideoJuego.route('/editar/<int:id>',methods= ["GET","POST"])
def editar(id):
    videoj = VideoJuego.query.get_or_404(id)
    videojForm = VideoJuegoForm(obj=videoj)
    if request.method == "POST":
        if videojForm.validate_on_submit():
            videojForm.populate_obj(videoj)
            db.session.commit()
            return redirect(url_for('appVideoJuego.inicio'))
    return render_template('editar.html',forma=videojForm)

@appVideoJuego.route('/eliminar/<int:id>')
def eliminar(id):
    videoj = VideoJuego.query.get_or_404(id)
    db.session.delete(videoj)
    db.session.commit()
    return redirect(url_for('appVideoJuego.inicio'))