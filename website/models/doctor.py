from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func # for date func.now()



class Doctor(db.Model, UserMixin):
    __tablename__ = 'doctor'
    id = db.Column("id", db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    patients = db.relationship('Patient', backref='doctor', lazy='dynamic')
    