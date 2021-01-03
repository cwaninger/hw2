"""
Database Model for Player
"""
# Library Imports

# App_specific imports
from database import db

class Usertype(db.Model):
    __tablename__ = "usertype"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Usertype %r>' % self.type_name