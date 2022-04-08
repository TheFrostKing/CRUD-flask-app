from imp import source_from_cache
from flask_sqlalchemy import SQLAlchemy
import datetime
 
db = SQLAlchemy()

class Application_Error(db.Model):
    __tablename__ = 'event_errors'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(80))
    date_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    source = db.Column(db.String(80))
    event_id = db.Column(db.Integer)


    def __repr__(self):
        return f"{self.level}:{self.date_time}:{self.source}:{self.event_id}"