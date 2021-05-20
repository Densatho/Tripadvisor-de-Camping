from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Local(db.Model):
    
    __tablename__ = 'local'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    rating_amount = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)