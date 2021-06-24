from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Perfil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    perfil = db.Column(db.String(40), unique=True, nullable=False)
    
    def get_all():
        try:
            res = db.session.query(Perfil).all() 
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res       
    
    def __repr__(self) -> str:
        return f'{self.perfil}'