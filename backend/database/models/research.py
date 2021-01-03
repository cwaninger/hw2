"""
Database Model for Research
"""
# Library Imports

# App_specific imports
from database import db

associative_table = Table('associative', Base.metadata,
    Column('research_id', Integer, ForeignKey('research.id'))
    Column('requires_id', Integer, ForeignKey('research.id'))
)

class Research(db.Model):
    __tablename__ = "research"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    research_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    research_points = db.Column(db.Integer, nullable=False)
    research_time = db.Column(db.Integer, nullable=False)
    race = db.relationship("Race", backref="research", lazy=True)
    score = db.Column(db.Integer, nullable=False, default=0)
    research_level = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Research %r>' % self.race_name

