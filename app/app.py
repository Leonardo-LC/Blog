import datetime
from dbm import error
from functools import wraps
from flask import session, redirect, url_for
from flask import Flask, send_from_directory, render_template, request, redirect, session, url_for, flash
#from app.controllers.application import Application
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from controllers.receitas_controller import adicionar_receita
from controllers.upload_controller import allowed_file, save_uploaded_file
#----------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = 'senhasecreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = 'static/img'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
db = SQLAlchemy(app)

class Receitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique= True, nullable=False) #Título da receita
    descricao = db.Column(db.Text, nullable=False)
    foto = db.Column(db.String(100))

@app.route('/')
def home():
    return render_template('base.html')

#Crud
@app.route('/adicionar', methods=['POST'])
def adicionar_receita_route():
    return adicionar_receita(request, db, Receitas)

#cRud
@app.route('/home')
def ler_receita():
    receitas = Receitas.query.all()
    return render_template('post.html', receitas=receitas)

#crUd
@app.route('/update/<int:receitas_id>', methods=['POST'])
def atualizar_receita(receitas_id):
    receita = Receitas.query.get(receitas_id)

    if receita:
        receita.description = request.form['description']
        receita.descricao = request.form['descricao']
        db.session.commit()
    return redirect('/home')


#cruD
@app.route('/delete/<int:receitas_id>', methods=['POST'])
def deletar_receita(receitas_id):
    receita = Receitas.query.get(receitas_id)

    if receita:
        db.session.delete(receita)
        db.session.commit()
    return redirect('/home')



#-----------------------------------------------------------------------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)