from app import db

class Ron(db.Model):
    id    = db.Column(db.Integer,primary_key=True)
    Marca = db.Column(db.String(255))

class Sidras(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Nombre = db.Column(db.String(255))
    Precio = db.Column(db.String(255))

class Vinos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Nombre = db.Column(db.String(255))
    Precio = db.Column(db.String(255))
    Marca = db.Column(db.String(255))