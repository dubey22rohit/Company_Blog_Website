from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from Company_Blog.core.views import core
from Company_Blog.error_pages.handlers import error_pages
from Company_Blog.users.views import users
app.register_blueprint(error_pages)
app.register_blueprint(core)
app.register_blueprint(users)