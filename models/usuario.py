from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class User(db.Model):
    
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    admin = db.Column(db.Boolean(), default=0, nullable=False)
    