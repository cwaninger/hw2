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

from database.models.usertype import Usertype as DBUsertype
from api.endpoints.user import usermodel
from api.controllers.usertype import create_usertype

# Namespace Definition
ns = api.namespace('usertypes', description='User Account Types')

# Serializer
usertypemodel = api.model('Usertype', {
    'id': fields.Integer(readOnly=True, description='The unique identifier for User'),
    'type_name': fields.String(required=True, description='Firstname of the User'),
    'description': fields.String(required=True, description='Lastname of the User'),
    'users': fields.List(fields.Nested(usermodel), required=False)
})

@ns.route('/')
class Usertypes(Resource):
    """
    Represents all Endpoints for all Usertypes
    """
    @api.marshal_with(usertypemodel)
    def get(self):
        """
        Returns list of all UserTypes
        """
        return DBUsertype.query.all()

    @api.expect(usertypemodel)
    def post(self):
        """
        Creates a new Usertype
        """
        new_type = create_usertype(request.json)
        return new_type.id , 201

@ns.route('/<int:id>')
class User(Resource):
    """
    Represents All Endpoints of specified Usertypes
    """
    @api.marshal_with(usertypemodel)
    def get(self, id):
        """
        Gets a specific Usertype
        """
        return DBUsertype.query.filter(DBUsertype.id == id).one(), 201