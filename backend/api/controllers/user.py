# Library Imports
from os import environ
import subprocess
from werkzeug.security import generate_password_hash

# App_specific imports
from utils.mail import sendmail
from utils.logging import filelogger
from database.models.user import User
from database import db

def create_password(length=16):
    # Create Password
    p = subprocess.Popen(["pwgen", "-cnB1", f"{length}"], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    if err:
        filelogger.debug("There was an error while generating the password")
        return {'code': '99', 'message': 'Error generating password'}, 400
    password_plain = output.decode('utf-8').split()[0]
    
    return generate_password_hash(password_plain)

def create_user(json_data):
    """
    Creates a User the proper way and sends an email to them
    Args:
        email: email of the User
        password: password hash for the db
        first_name: first Name of User
        last_name: last name of User
        type_id: int of Usertype Admin(1)/User(2)/Photographer(3)
        password_plain: password passed through to send in email

    Returns:
        obj: User
    """

    user = User(
        email=json_data["email"], 
        firstName=json_data["firstname"], 
        lastName=json_data["lastname"]
    )
    db.session.add(user)
    db.session.flush()

    filelogger.info("New User created with following data: email: %s, firstName; %s, lastName: %s"
        % (json_data["email"], json_data["firstname"], json_data["lastname"]))
    mail_data = {
        "email": json_data["email"],
        "firstname": json_data["firstname"],
        "lastname": json_data["lastname"],
        "password": create_password()
    }

    # If type is not photographer and we not on development
    if environ.get('FLASK_ENV') == 'production':
        #Send Mail to new user
        sendmail("my subject", [json_data["email"]], mail_data)
        filelogger.debug("Register Mail send to %s" % json_data["email"])
    db.session.commit()
    return user