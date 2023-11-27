import flask
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
import time



app = Flask(__name__)
app.config['SECRET_KEY'] = 'niknik7777777'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(50), nullable=True)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
class Registr(FlaskForm):
    login = StringField("Name: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[Email()])

@app.route('/main')
@login_required
def index1():
    return render_template('main.html')

@app.route('/', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        name = request.form.get('login')
        psw = request.form.get('password')
        try:
            user = Users.query.filter_by(login=name).first()
            if user.psw == psw:
                login_user(user)
                return render_template('main.html')
            else:
                flash('Неправильный логин или пароль', category='error')
        except:
            flash('Неправильный логин или пароль', category='error')
    s = Registr()
    return render_template('registration.html', form=s)


@app.route('/lesson')
@login_required
def index3():
    return render_template('lesson.html')

@app.route('/quit')
@login_required
def index4():
    logout_user()
    return render_template('quit.html'), {"Refresh": "5; url=/"}

@app.errorhandler(401)
def not_found_error(error):
    return render_template('error404.html')

@app.route('/python1')
@login_required
def index21():
    return render_template('python1.html')

@app.route('/python2')
@login_required
def index22():
    return render_template('python2.html')

@app.route('/python3')
@login_required
def index23():
    return render_template('python3.html')

@app.route('/python4')
@login_required
def index24():
    return render_template('python4.html')

@app.route('/python5')
@login_required
def index25():
    return render_template('python5.html')

@app.route('/python6')
@login_required
def index26():
    return render_template('python6.html')

@app.route('/python7')
@login_required
def index27():
    return render_template('python7.html')

@app.route('/python8')
@login_required
def index28():
    return render_template('python8.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404404.html')

if __name__ == '__main__':
    app.run()