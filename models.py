from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
db = SQLAlchemy()

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