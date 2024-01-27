from .. import db
from flask_login import UserMixin
#from datetime import datetime
from .medicals_record import MedicalRecord
from .patient import Patient
from .doctor import Doctor
#from .. import encrypt_data, decrypt_data

# create table in database for assigning roles
#roles_users = db.Table('roles_users',
        #db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        #db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))  

#class Role(db.Model):
    #__tablename__ = 'role'
    #id = db.Column("id", db.Integer, primary_key=True)
    #name = db.Column(db.String(150))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column("id", db.Integer, primary_key=True) 
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    #date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    #roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    doctors = db.relationship('Doctor', backref='user', lazy='dynamic')
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    """ def __init__(self, email, password):
        self.email = email
        self.password = password """
    # posts = db.relationship('Post', backref='user', lazy=True)

""" def set_sensitive_data(self, key, sensitive_data):
        self.encrypted_data = encrypt_data(key, sensitive_data)

    def get_sensitive_data(self, key):
        return decrypt_data(key, self.encrypted_data) """