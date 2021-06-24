from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship 
from config import app_active, app_config
from .local import Local

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Announce(db.Model):
    
    __tablename__ = 'announce'
    
    id = db.Column(db.Integer, primary_key=True)
    relacao = db.Column(db.Integer, db.ForeignKey(Local.id), nullable=False)
    local = relationship(Local)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(240), nullable=False)
    
    
    def get_all():
        try:
            res = db.session.query(Announce).all() 
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res   
    
    def __repr__(self) -> str:
        return f'{self.local} - {self.price} - {self.description}'