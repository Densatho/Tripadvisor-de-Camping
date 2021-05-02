from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/401')
def erro401():
    return render_template('401.html')


@app.route('/404')
def erro404():
    return render_template('404.html')


@app.route('/500')
def erro500():
    return render_template('500.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin/charts')
def admin_charts():
    return render_template('charts.html')


@app.route('/login')
def admin_login():
    return render_template('login.html')


@app.route('/password')
def admin_password():
    return render_template('password.html')


if __name__ == '__main__':
    app.run(debug=True)