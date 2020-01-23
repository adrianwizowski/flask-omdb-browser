"""Base application module."""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import omdb
from oauthlib.oauth2 import WebApplicationClient

from flask_app.config import API_KEY, GOOGLE_CLIENT_ID
from flask_app.user import User

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()

omdb_client = omdb.OMDBClient(apikey=API_KEY)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager.init_app(app)


# OAuth 2 client setup
oauth_client = WebApplicationClient(GOOGLE_CLIENT_ID)
