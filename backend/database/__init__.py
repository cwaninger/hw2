"""
Contains all basic db functions that might be required
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

migrate = Migrate(db=db)
Base = declarative_base()