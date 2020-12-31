"""
Database Model for Player
"""
# Library Imports
from flask import current_app

# App_specific imports
from utils.logging import filelogger
from database import db

class Player(db.Model):
    __tablename__ = "player"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_name = db.Column(db.String(20), nullable=False)

    description = db.Column(db.Text, nullable=True)
    #start_position = db.
    score = db.Column(db.Integer, nullable=False, default=0)
    score_average = db.Column(db.Integer, nullable=False, default=0)

    # Relations
    user_login = db.relationship("User", backref="player", lazy="dynamic")
    race = db.relationship("Race", backref="player", lazy=True)

    # Resources
    gold = db.Column(db.BigInteger, nullable=False, default=current_app.config["HW2_START_GOLD"])
    wood = db.Column(db.BigInteger, nullable=False, default=current_app.config["HW2_START_RES"])
    stone = db.Column(db.BigInteger, nullable=False, default=current_app.config["HW2_START_RES"])
    iron = db.Column(db.BigInteger, nullable=False, default=0)
    research_points = db.Column(db.BigInteger, nullable=False, default=current_app.config["HW2_START_RESEARCH_POINTS"])

    def __repr__(self):
        return '<User %r>' % self.id