from werkzeug.security import generate_password_hash, check_password_hash
#from werkzeug import generate_password_hash, check_password_hash
from Lost_and_Found.appConfig.appFactory import db

from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80),nullable =False)
    lastname = db.Column(db.String(80),nullable =False)
    password = db.Column(db.String(80),nullable =False)
    #pwdhash = db.Column(db.String(120))
    #username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    #phone_number = db.Column(db.Integer, nullable = False)
    def __init__(self, firstname, lastname,email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        #self.phone_number = phone_number.title()
        self.password = password.title()
        #self.username = username.title()

    '''def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):'''

    def __repr__(self):
        return '<User %r>' % self.email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.uid)
