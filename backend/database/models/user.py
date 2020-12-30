"""
Database Models are kept here together with references to the database and auth object.
"""
# Library Imports

# App_specific imports
from utils.logging import filelogger
from database import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(15), nullable=False)
    lastName = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    verified = db.Column(db.Boolean, default=False, nullable=True)
    password_hash = db.Column(db.String, nullable=True)
    #type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    #tokens = db.relationship("Token", backref="user", lazy='dynamic')

    # @classmethod
    # def create(cls, email: str, password: str, first_name: str, last_name: str, type_id: str, password_plain: str):
    #     """
    #     Creates a User the proper way and sends an email to them
    #     Args:
    #         email: email of the User
    #         password: password hash for the db
    #         first_name: first Name of User
    #         last_name: last name of User
    #         type_id: int of Usertype Admin(1)/User(2)/Photographer(3)
    #         password_plain: password passed through to send in email

    #     Returns:
    #         obj: User
    #     """

    #     user = User(email=email, firstName=first_name, lastName=last_name, password_hash=password,
    #                   type_id=type_id)
    #     db.session.add(user)
    #     db.session.flush()

    #     filelogger.info("New User created with following data: email: %s, firstName; %s, lastName: %s, type: %d"
    #         % (email, first_name, last_name, type_id))
    #     mail_data = {
    #         "email": email,
    #         "firstname": firstname,
    #         "lastname": lastname,
    #         "password": password
    #     }

    #     # If type is not photographer and we not on development
    #     if environ.get('FLASK_ENV') == 'production':
    #         #Send Mail to new user
    #         sendmail("my subject", [email], mail_data)
    #         filelogger.debug("Register Mail send to %s" % email)
    #     return user