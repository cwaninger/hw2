# Library Imports

# App_specific imports
from utils.logging import filelogger
from database.models.unit import Unit
from database import db

def create_unit(json_data):
    unit = Unit(

    )
    db.session.add(unit)
    db.session.flush()
    db.session.commit()
    return unit