from .. import db
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