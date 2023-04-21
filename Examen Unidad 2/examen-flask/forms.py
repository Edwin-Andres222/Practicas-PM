from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class VideoJuegoForm(FlaskForm):
    nombre = StringField('nombre',validators=[DataRequired()])
    descripcion = StringField('descripcion',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class LibroForm(FlaskForm):
    nombre = StringField('nombre',validators=[DataRequired()])
    descripcion = StringField('descripcion',validators=[DataRequired()])
    enviar = SubmitField('Enviar')