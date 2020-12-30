"""
Endpoint Specification of User
"""
# Library Imports
from flask import request #current_app
from flask_restplus import Resource

# App_specific imports
from utils.logging import filelogger
from api.restplus import api

from database.models.user import User

# Namespace Definition
ns = api.namespace('user', description='User Account Operations')

@ns.route('/')
class UserCollection(Resource):
    def get(self):
        """
        Returns list of all User Accounts
        """
        return "yess"
        users = User.query.all()
        return users