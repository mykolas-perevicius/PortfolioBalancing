from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ, path
from dotenv import load_dotenv
from flask import Flask
from Backend.models import db
from Backend.models.user import User

# Load environment variables from .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# Initialize the database and migration objects without an app
db = SQLAlchemy()
migrate = Migrate()

# Rest of your Flask app code goes here

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return '<User %r>' % self.username
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def serialize_with_password(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def serialize_with_password_and_token(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "token": self.token,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def serialize_with_token(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "token": self.token,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

def create_app(config_class='config.ConfigClass'):
    app = Flask(__name__)

    # Load configuration from the given class
    app.config.from_object(config_class)
    # Or load configuration from an environment variable pointing to a config file
    # app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    # Initialize the database and migration with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from yourapplication.api import api_bp  # Import your blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    # Add more blueprint registrations here

    return app

# Use this part only when running the app directly via 'python app.py'
if __name__ == '__main__':
    # Create an app by calling the create_app function
    app = create_app()
    
    # Run the app
    app.run(debug=True)