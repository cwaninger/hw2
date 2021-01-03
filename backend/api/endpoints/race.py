"""
Database Model for Races
"""
# Library Imports

# App_specific imports
from database import db

class Race(db.Model):
    __tablename__ = "race"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(50), nullable=True)
    player_id = db.relationship(db.Integer, db.ForeignKey("player.id"), nullable=True)
    unit_id = db.relationship(db.Integer, db.ForeignKey("unit.id"), nullable=True)

    def __repr__(self):
        return '<Race %r>' % self.race_name