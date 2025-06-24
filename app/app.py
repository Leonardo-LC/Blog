from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from models.cliente import Cliente
from models.animal import Animal
from    controllers.serializador import Serializador
import os

app = Flask(__name__)
app.secret_key = '123'

# Banco de dados JSON
db_clientes = Serializador("clientes.json")
db_pets = Serializador("pets.json")

# --- Rotas de Autenticação ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        clientes = db_clientes.get_models()
        for cliente in clientes:
            if cliente['email'] == email and check_password_hash(cliente['senha'], senha):
                session['user_email'] = email
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('meus_pets'))
        flash('E-mail ou senha incorretos!', 'danger')
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = generate_password_hash(request.form['senha'])

        if db_clientes.verify_email(email):
            flash('E-mail já cadastrado!', 'danger')
        else:
            novo_cliente = Cliente(nome, email, telefone)
            novo_cliente.senha = senha  # Adiciona a senha hash
            db_clientes.adicionar_cliente(novo_cliente)
            flash('Conta criada com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect(url_for('home'))

# --- Rotas de Pets ---
@app.route('/meus-pets')
def meus_pets():
    if 'user_email' not in session:
        return redirect(url_for('login'))

    pets = db_pets.get_models()
    user_pets = [pet for pet in pets if pet['dono_email'] == session['user_email']]
    return render_template('meus_pets.html', pets=user_pets)

@app.route('/adicionar-pet', methods=['GET', 'POST'])
def adicionar_pet():
    if 'user_email' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form['nome']
        especie = request.form['especie']
        idade = request.form['idade']
        novo_pet = Animal(nome, especie, idade, session['user_email'])
        db_pets.adicionar_pet(novo_pet)
        flash('Pet adicionado com sucesso!', 'success')
        return redirect(url_for('meus_pets'))
    return render_template('adicionar_pet.html')

# --- Rota Home ---
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs("models/controllers/database", exist_ok=True)
    app.run(debug=True)