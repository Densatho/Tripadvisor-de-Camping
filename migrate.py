from flask import Flask
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 
from config import app_active, app_config
from models.local import Local
from models.usuario import User
from models.anuncio import Announce

config = app_config[app_active]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app) 
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()