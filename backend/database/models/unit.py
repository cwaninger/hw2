"""
Database Model for Units
"""
# Library Imports

# App_specific imports
from database import db

class Unit(db.Model):
    __tablename__ = "unit"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unit_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Relationship
    race = db.relationship("race", backref="unit", lazy=True)

    # Stats
    level = db.Column(db.Integer, nullable=False, default=0)
    damage = db.Column(db.Integer, nullable=False, default=0)
    life = db.Column(db.Integer, nullable=False, default=0)
    speed = db.Column(db.Integer, nullable=False, default=0)
    score = db.Column(db.Integer, nullable=False, default=0)
    bonus_damage_1 = db.Column(db.Integer, nullable=False, default=0)
    bonus_damage_2 = db.Column(db.Integer, nullable=False, default=0)
    bonus_damage_3 = db.Column(db.Integer, nullable=False, default=0)

    # Costs
    gold = db.Column(db.Integer, nullable=False, default=0)
    shortrange = db.Column(db.Integer, nullable=False, default=0)
    longrange = db.Column(db.Integer, nullable=False, default=0)
    armor = db.Column(db.Integer, nullable=False, default=0)
    horse = db.Column(db.Integer, nullable=False, default=0)
    maintenance = db.Column(db.Integer, nullable=False, default=0)
    training = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Unit %r>' % self.unit_name