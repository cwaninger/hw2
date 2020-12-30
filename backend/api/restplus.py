"""
Database Models are kept here together with references to the database and auth object.
"""
# Library Imports
from flask import current_app
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
import traceback

# App_specific imports
from utils.logging import filelogger

api = Api(version='1.0', title='Holy-Wars 2 API',
          description='Specification of the HW2-API')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not os.environ.get('FLASK_DEBUG') or not current_app.config["DEBUG"]:
        return {'message': message}, 500

@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404

# Import all Endpoint Namespaces
from api.endpoints.user import ns as user_namespace

# Add all Endpoint Namespaces to API
api.add_namespace(user_namespace)