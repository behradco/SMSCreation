from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "da807d45fe597024e301da7b7426c0a3"

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from base import routes
