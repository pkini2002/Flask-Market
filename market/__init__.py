from enum import unique
from unicodedata import name
import bcrypt
from flask import Flask
from flask import render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'

bcrypt=Bcrypt(app)

login_manager=LoginManager(app)

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from market import routes
app.config['SECRET_KEY']='5132631d613670e1a5e585e1'

login_manager.login_view="login_page"
login_manager.login_message_category="info"