from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import TEXT, null
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)

    # @property
    # def password(self):
    #     raise AttributeError('password is not readable attribute')

    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)
    
class Events_model(db.Model):
    __tablename__ = 'event_errors'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(80))
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.String(80))
    event_id = db.Column(db.Integer())

    def __init__(self, level,date_time,source,event_id):
        self.level = level
        self.date_time = date_time
        self.source = source
        self.event_id = event_id
 

    def __repr__(self):
        return f"{self.id}:{self.level}:{self.date_time}:{self.source}:{self.event_id}"