from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
admin = Admin(app, name='infinity', template_mode='bootstrap3')
db = SQLAlchemy(app)
manager = Manager(app)

from .models import Faction

admin.add_view(ModelView(Faction, db.session))

db.create_all()

from app import views
