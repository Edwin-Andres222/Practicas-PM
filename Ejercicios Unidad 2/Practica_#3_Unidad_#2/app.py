from flask import Flask
from flask_migrate import Migrate
from database import db
import logging
from config import BasicConfig
from routes.Ron.Ron import appRon
from routes.Sidras.Sidras import appSidras
from routes.Vinos.Vinos import appVinos, appVinos2

app = Flask(__name__)
app.register_blueprint(appRon)
app.register_blueprint(appSidras)
app.register_blueprint(appVinos)
app.register_blueprint(appVinos2)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="debug.log")