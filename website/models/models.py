from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func # for date func.now()
from .medicals_record import MedicalRecord
from .. import encrypt_data, decrypt_data

# create table in database for assigning roles
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))  

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(150))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column("id", db.Integer, primary_key=True) 
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    #medical_records = db.relationship('MedicalRecord') # this is a list of medical records
    
    """ def __init__(self, email, password):
        self.email = email
        self.password = password """
    # posts = db.relationship('Post', backref='user', lazy=True)
    def set_sensitive_data(self, key, sensitive_data):
        self.encrypted_data = encrypt_data(key, sensitive_data)

    def get_sensitive_data(self, key):
        return decrypt_data(key, self.encrypted_data)