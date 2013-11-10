import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from config import basedir
from momentjs import momentjs

app = Flask(__name__)
app.config.from_object('config')

app.jinja_env.globals['momentjs'] = momentjs #Allow Jinja templates to use momentjs

db = SQLAlchemy(app)

mail = Mail(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models