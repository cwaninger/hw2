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

from database.models.user import User as DBUser
from api.controllers.user import create_user

# Namespace Definition
ns = api.namespace('users', description='User Account Operations')

# Serializer
usermodel = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier for User'),
    'firstname': fields.String(required=True, description='Firstname of the User'),
    'lastname': fields.String(required=True, description='Lastname of the User'),
    'email': fields.String(required=True, description='Lastname of the User')
})

@ns.route('/')
class UserCollection(Resource):
    """
    Represents all Endpoints for all Users
    """
    def get(self):
        """
        Returns list of all User Accounts
        """
        users = DBUser.query.all()
        print (users)
        return users

    @api.expect(usermodel)
    def post(self):
        """
        Creates a new User
        """
        new_user = create_user(request.json)
        return new_user.id , 201

@ns.route('/<int:id>')
class User(Resource):
    """
    Represents All Endpoints of specified Users
    """
    @api.marshal_with(usermodel)
    def get(self, id):
        """
        Gets a specific User
        """
        return DBUser.query.filter(DBUser.id == id).one(), 201

