from .. import db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from ..models import User  # Import your models

admin = Admin()

class MyModelView(ModelView):
    column_display_pk = True
    column_searchable_list = ['email', 'first_name', 'last_name']
    column_filters = ['date_registered']

admin.add_view(MyModelView(User, db.session))