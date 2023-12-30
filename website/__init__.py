from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin

db = SQLAlchemy()
DB_NAME = "database.db"
admin = Admin()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aesmodels'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    admin.init_app(app)  # Initialize Flask-Admin

    migrate = Migrate(app, db)

    from .views.views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models.models import User
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # redirect to login page if not logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # get user by id
    
    # Register models with Flask-Admin
    from flask_admin.contrib.sqla import ModelView
    from .models.models import User, MedicalRecord, Patient, Doctor

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(MedicalRecord, db.session))
    admin.add_view(ModelView(Patient, db.session))
    admin.add_view(ModelView(Doctor, db.session))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')