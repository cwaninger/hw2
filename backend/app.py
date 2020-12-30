"""
Creates the app context for the Flask app to work off of.
Initialises Logging, DB access, backend controllers, mail and model migrations.
"""

# Library Imports
from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from flask_swagger import swagger
import os

# App_specific imports
from database import db
from utils.mail import mail
from utils.logging import initLogging
from api.restplus import api
#from api import generate_endpoints

def configure_app():
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_pyfile('config.py')
    else:
        app.config.from_pyfile('config-dev.py')

def init_app():
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)

    initLogging()
    CORS(app)
    #migrate.init_app(app, db)
    app.register_blueprint(blueprint)
    db.init_app(app)

app = Flask(__name__, instance_relative_config=True)
configure_app()
init_app()
