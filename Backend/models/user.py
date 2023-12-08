from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Portfolio analysis module fields
    risk_tolerance = db.Column(db.String(50))  # e.g., "low", "medium", "high"
    investment_goals = db.Column(db.Text)  # User can describe their investment goals
    investment_horizon = db.Column(db.String(50))  # e.g., "short", "medium", "long"
    investment_experience = db.Column(db.String(50))  # e.g., "none", "limited", "extensive"
    investment_knowledge = db.Column(db.String(50))  # e.g., "none", "limited", "extensive"
    liquidity_needs = db.Column(db.String(50))  # e.g., "low", "medium", "high"

    # Fields for linking to other tables/models
    portfolios = db.relationship('Portfolio', backref='user', lazy=True)
    transactions = db.relationship('Transaction', backref='user', lazy=True)
    holdings = db.relationship('Holding', backref='user', lazy=True)
    watchlists = db.relationship('Watchlist', backref='user', lazy=True)
    alerts = db.relationship('Alert', backref='user', lazy=True)
    messages = db.relationship('Message', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Portfolio(db.Model):
    # Define the Portfolio model here
    pass

class Transaction(db.Model):
    # Define the Transaction model here
    pass

class Holding(db.Model):
    # Define the Holding model here
    pass

class Watchlist(db.Model):
    # Define the Watchlist model here
    pass

class Alert(db.Model):
    # Define the Alert model here
    pass

class Message(db.Model):
    # Define the Message model here
    pass

class Notification(db.Model):
    # Define the Notification model here
    pass
    
    
    
    
