import re
import string
import secrets
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models.models import User
from .models.patient import Patient
from .models.doctor import Doctor
from .models.medicals_record import MedicalRecord
from .static import encrypt_data, decrypt_data

auth = Blueprint('auth', __name__)

# Generate a random 32 bytes key for AES-256
key = secrets.token_bytes(32)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                
                    # Redirect based on user role
                #if 'doctor' in [role.name for role in user.roles]:
                    #return redirect(url_for('doctor_dashboard'))
                # elif 'patient' in [role.name for role in user.roles]:
                    # return redirect(url_for('patient_dashboard'))
                #else:
                    # Handle other roles or a default view
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user) 

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password = request.form.get('password1')
        confirm_password = request.form.get('password2')
        #role = request.form.get('role')  # Get selected role

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            flash('Invalid email format.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password) or not any(char in string.punctuation for char in password):
            flash('Password must be at least 7 characters and contain a mix of uppercase, lowercase, numbers, and special characters.', category='error')
        else:
            # Create user and assign role
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='pbkdf2:sha256'))
            #role = Role.query.filter_by(name=role).first()
            #if role:
               #new_user.roles.append(role)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
            
    return render_template("sign_up.html", user=current_user)

""" @auth.route('/doctor-dashboard')
@login_required
def doctor_dashboard():

    return render_template('doctor.html', user=current_user) """

""" @auth.route('/patient-dashboard')
@login_required
def patient_dashboard():

    return render_template('patient.html', user=current_user) """

@auth.route('/doctor', methods=['GET', 'POST'])
def doctor():
    if request.method == 'POST':
        doctor_name = request.form.get('doctor_name')
        doctor_dob = request.form.get('doctor_dob')
        doctor_gender = request.form.get('gender')
        doctor_phone = request.form.get('doctor_phone')
        doctor_email = request.form.get('doctor_email')

        new_doctor = Doctor(doctor_name=doctor_name, 
                            doctor_dob=doctor_dob, 
                            doctor_gender=doctor_gender, 
                            doctor_phone=doctor_phone,
                            doctor_email=doctor_email)
        db.session.add(new_doctor)
        db.session.commit()
        flash('Doctor added!', category='success')  


    return render_template("doctor.html", user=current_user) 

@auth.route('/medical-record', methods=['GET', 'POST'])
def medical_record():
    if request.method == 'POST':
        blood_type = request.form.get('blood_type')
        blood_pressure = request.form.get('blood_pressure')
        weight = request.form.get('weight')
        height = request.form.get('height')
        disease_history = request.form.get('disease_history')
        drug_sensitive = request.form.get('drug_sensitive')

        new_medical_record = MedicalRecord(blood_type=blood_type, 
                                           blood_pressure=blood_pressure, 
                                           weight=weight, height=height, 
                                           disease_history=disease_history, 
                                           drug_sensitive=drug_sensitive)
        db.session.add(new_medical_record)
        db.session.commit()
        flash('Medical record added!', category='success')
    return render_template("medical_record.html", user=current_user) 

@auth.route('/medical-record-view', methods=['GET', 'POST'])
def medical_record_view():
    patients = Patient.query.all()
    # data= request.form
    # print(data)
    return render_template("medical_record_view.html", patients=patients, user=current_user)