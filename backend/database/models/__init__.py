"""
Database Models are kept here together with references to the database and auth object.
"""
# Library Imports
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()
auth = HTTPBasicAuth()

migrate = Migrate(db=db)
Base = declarative_base()