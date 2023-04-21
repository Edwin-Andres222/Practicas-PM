import logging
from flask import Flask
from flask_migrate import Migrate
from config import BasicConfig
from models import db
from routes.videojuegos.videojuego import appVideoJuego

app = Flask(__name__)

app.register_blueprint(appVideoJuego)
app.config.from_object(BasicConfig)

db.init_app(app)
migrate = Migrate()
logging.basicConfig(level=logging.DEBUG, filename = "debug.log")
migrate.init_app(app,db)