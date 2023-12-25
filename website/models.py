from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func # for date func.now()

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    patient_name = db.Column(db.String(150))
    patient_dob = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    address = db.Column(db.String(150))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(150))
    social_security = db.Column(db.String(150))
    helth_insurance = db.Column(db.String(150))
    martial_status = db.Column(db.String(150))
    occupation = db.Column(db.String(150))
    blood_type = db.Column(db.String(150))
    blood_pressure = db.Column(db.String(150))
    weight = db.Column(db.String(150))
    height = db.Column(db.String(150))
    disease_history = db.Column(db.String(150))
    drug_sensitivity = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user.id is the table name



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
