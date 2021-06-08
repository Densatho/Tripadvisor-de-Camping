from flask import Flask, render_template, request, redirect
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from admin.admin import start_views
from controllers.usuario import UsuarioController

# A variável config recebe a atribuição do ambiente ativo.
config = app_config[app_active]

# Método create_app que recebe como argumento com todas as configurações da aplicação.
def create_app(config_name):

    # A variável app recebe uma instância de Flask, passando a configuração da localização dos templates. Pode 
    # receber diversas configurações.
    app = Flask(__name__, template_folder='templates')

    # O atributo secret_key da aplicação app, recebe a configuração da chave secreta do arquivo config.py, por meio da variável config e atributo SECRET.
    app.secret_key = config.SECRET 

    # Efetua o carregamento do arquivo config.py
    app.config.from_object(app_config[config_name]) 
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    db = SQLAlchemy(config.APP)
    start_views(app, db)
    db.init_app(app)


    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/search/')
    def search():
        return render_template('search.html')


    @app.route('/401/')
    def erro401():
        return render_template('401.html')


    @app.route('/404/')
    def erro404():
        return render_template('404.html')


    @app.route('/500/')
    def erro500():
        return render_template('500.html')


    @app.route('/admin/')
    def admin():
        return render_template('admin.html')


    @app.route('/admin/charts/')
    def admin_charts():
        return render_template('charts.html')


    @app.route('/login/')
    def login():
        return render_template('login.html')


    @app.route('/login/', methods=['POST'])
    def login_post():
        user = UsuarioController()
        email = request.form['email']
        password = request.form['password']
        resultado = user.login(email, password)
        if resultado:
            return redirect('/admin')
        else:
            data = {'status': 401, 'msg': 'Dados incorretos', 'type': None}
            return render_template('login.html', data)


    @app.route('/password/')
    def admin_password():
        return render_template('password.html')
    
    return app


if __name__ == '__main__':
    app.run(debug=True)