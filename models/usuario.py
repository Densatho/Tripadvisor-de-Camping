from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship 
from config import app_active, app_config
from models.perfil import Perfil
from passlib.hash import pbkdf2_sha256

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class User(db.Model):
    
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True) 
    recovery_code=db.Column(db.String(100),nullable=True) 
    active=db.Column(db.Boolean(),default=1,nullable=False) 
    relacao=db.Column(db.Integer,db.ForeignKey(Perfil.id),nullable=False)
    perfil = relationship(Perfil)
    
    def __repr__(self) -> str:
        return f'{self.id} - {self.username}'
    
     # Métodos adicionados para configuração posterior
    def get_usuario_by_email(self): 
        # Método para validar se usuário existe ou não
        return ' '
        
    def get_all():
        try:
            res = db.session.query(User).all() 
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res        

    def get_usuario_by_id(self): 
        # Método para listar dados do usuário perfil
        return ' '

    def update_usuario(self, obj): 
        # Método para atualizar o usuário 
        return ' '

    # Adicionando os métodos para criptografia de senha
    # Metodo de conversão de senha de string para string criptografada
    def hash_password(self, password): 
        try:
            return pbkdf2_sha256.hash(password) 
        except Exception as e:
            print("Erro ao tentar criptografar a senha %s" % e) 

    # Método para atualizar senha
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    # Método para verificar se a senha informada é igual a que está no banco de dados
    def verify_password(self, password_no_hash, password_database): 
        try:
            return pbkdf2_sha256.verify(password_no_hash, password_database)
        except ValueError:
            return False