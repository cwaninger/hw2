# Library Imports

# App_specific imports
from utils.logging import filelogger
from database.models.usertype import Usertype
from database import db

def create_usertype(json_data):
    usertype = Usertype(
        type_name=json_data["type_name"], 
        description=json_data["description"], 
    )
    db.session.add(usertype)
    db.session.flush()
    db.session.commit()
    return usertype