"""
Endpoint Specification of User
"""
# Library Imports
from flask import request #current_app
from flask_restplus import Resource, reqparse
from flask_restplus import fields

# App_specific imports
from utils.logging import filelogger
from api.restplus import api

from database.models.unit import Unit as DBUnit

# Namespace Definition
ns = api.namespace('units', description='Units')

# Serializer
unitmodel = api.model('unit', {
    'id': fields.Integer(readOnly=True, description='The unique identifier for User'),
    'unit_name': fields.String(required=True, description='Name of the Unit'),
    'description': fields.String(required=True, description='Description of the User'),
})

@ns.route('/')
class Units(Resource):
    """
    Represents all Endpoints for all Units
    """
    def get(self):
        """
        Returns list of all UserTypes
        """
        return DBUnit.query.all()

    @api.expect(usertypemodel)
    def post(self):
        """
        Creates a new Usertype
        """
        new_type = create_usertype(request.json)
        return new_type.id , 201

@ns.route('/<int:id>')
class Unit(Resource):
    """
    Represents All Endpoints of specified Units
    """
    @api.marshal_with(usertypemodel)
    def get(self, id):
        """
        Gets a specific Usertype
        """
        return DBUnit.query.filter(DBUnit.id == id).one(), 201