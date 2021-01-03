"""
Database Model for User
"""
# Library Imports

# App_specific imports
from utils.logging import filelogger
from database import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(15), nullable=False)
    lastname = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=True)
    user_type_id = db.Column(db.Integer, db.ForeignKey('usertype.id'))

    # Status
    last_seen = db.Column(db.Integer, nullable=True)
    last_ip = db.Column(db.String(15), nullable=True)

    # Registering
    activation_key = db.Column(db.String(50), nullable=True, default=0)
    activation_time = db.Column(db.Integer, nullable=True, default=0)
    register_time = db.Column(db.Integer, nullable=False)
    register_mail = db.Column(db.String(50), nullable=False, unique=True)
    verified = db.Column(db.Boolean, default=False, nullable=True)

    # Relations
    user_type = db.relationship("Usertype", backref="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id