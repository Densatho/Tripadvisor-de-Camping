from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from .local import Local

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Announce(db.Model):
    
    __tablename__ = 'announce'
    
    id = db.Column(db.Integer, primary_key=True)
    local = db.Column(db.Integer, db.ForeignKey(Local.id), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(240), nullable=False)