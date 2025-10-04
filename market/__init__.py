from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# Use a simple secret key for development. In production, load from environment variable.
app.config['SECRET_KEY'] = 'dev_secret_key_change_me'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes
from market.models import User


@login_manager.user_loader
def load_user(user_id):
	try:
		return User.query.get(int(user_id))
	except Exception:
		return None
from market import routes
