from .. import db
from flask_admin.contrib.sqla import ModelView

class MedicalRecord(db.Model):
    __tablename__ = 'medical_record'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    blood_type = db.Column(db.String(40))
    blood_pressure = db.Column(db.String(40))
    weight = db.Column(db.String(40))
    height = db.Column(db.String(40))
    disease_history = db.Column(db.Text)
    drug_sensitive = db.Column(db.Text)
    doctor_name = db.Column(db.String(150))
    patient = db.relationship('Patient', back_populates='medical_records')

class MedicalRecordView(ModelView):
    form_columns = ['patient', 
                    'blood_type', 
                    'blood_pressure', 
                    'weight', 
                    'height', 
                    'disease_history', 
                    'drug_sensitive', 
                    'doctor_name']