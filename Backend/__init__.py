from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from .app import create_app

api_bp = Blueprint('api', __name__)
db = SQLAlchemy()

from Backend.api import users  # Import the users routes
from . import auth  # Import the auth routes
from . import posts  # Import the posts routes