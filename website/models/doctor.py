from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func # for date func.now()



class Doctor(db.Model, UserMixin):
    __tablename__ = 'doctor'
    id = db.Column("id", db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    patients = db.relationship('Patient', backref='doctor', lazy='dynamic')
    doctor_name = db.Column(db.String(150))
    doctor_dob = db.Column(db.Date)
    doctor_gender = db.Column(db.String(10))
    doctor_phone = db.Column(db.String(20))
    doctor_email = db.Column(db.String(150), unique=True)
