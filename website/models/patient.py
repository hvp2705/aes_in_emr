from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func # for date func.now()
from .medicals_record import MedicalRecord


# Define the Patient model
class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(150))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(150), unique=True)
    social_security_number = db.Column(db.String(20))
    health_insurance_number = db.Column(db.String(20))
    marital_status = db.Column(db.String(20))
    occupation = db.Column(db.String(150))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    medical_records = db.relationship('MedicalRecord', backref='patient', lazy='dynamic')

    
    """ def __init__(self, email, password):
        self.email = email
        self.password = password """
    # posts = db.relationship('Post', backref='user', lazy=True)
