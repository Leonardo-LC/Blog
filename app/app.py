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
#----------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Receitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique= True, nullable=False)

@app.route('/')
def home():
    return render_template('base.html')

#Crud
@app.route('/adicionar', methods=['POST'])
def adicionar_receita():
    description = request.form['description']

    receita_existente = Receitas.query.filter_by(description = description).first()
    if receita_existente:
        return 'Erro: Esta receita já foi cadastrada!', 400

    nova_receita = Receitas(description = description)
    db.session.add(nova_receita)
    db.session.commit()
    return redirect('/home')

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