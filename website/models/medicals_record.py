from .. import db
from sqlalchemy.sql import func # for date func.now()

class MedicalRecord(db.Model):
    __tablename__ = 'medical_record'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    blood_type = db.Column(db.String(10))
    blood_pressure = db.Column(db.String(20))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    disease_history = db.Column(db.Text)
    drug_sensitive = db.Column(db.Text)
    doctor_name = db.Column(db.String(150))
    doctor_phone = db.Column(db.String(20))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))