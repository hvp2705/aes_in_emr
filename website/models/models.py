from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func # for date func.now()
from .medicals_record import MedicalRecord


class User(db.Model, UserMixin):
    id = db.Column("id", db.Integer, primary_key=True) 
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    medical_records = db.relationship('MedicalRecord') # this is a list of medical records
    
    """ def __init__(self, email, password):
        self.email = email
        self.password = password """
    # posts = db.relationship('Post', backref='user', lazy=True)
