from flask import Flask, render_template, request, redirect, url_for
from models.cliente import Cliente
import json
import os

app = Flask(__name__)
app.secret_key = '123'

# Banco de dados
DB_FILE = 'clientes_db.json'


def carregar_clientes():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            dados = json.load(f)
            return [Cliente(**cliente) for cliente in dados]
    return []


def salvar_clientes(clientes):
    with open(DB_FILE, 'w') as f:
        json.dump([cliente.to_dict() for cliente in clientes], f)


@app.route('/lista')
def index():
    clientes = carregar_clientes()
    return render_template('index.html', clientes=clientes)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    clientes = carregar_clientes()

    novo_cliente = Cliente(
        nome=request.form['nome'],
        telefone=request.form['telefone']
    )
    novo_cliente.adicionar_pet(
        nome_pet=request.form['nome_pet'],
        tipo_pet=request.form['tipo_pet']
    )

    clientes.append(novo_cliente)
    salvar_clientes(clientes)
    return redirect(url_for('index'))


@app.route('/remover/<int:cliente_id>')
def remover(cliente_id):
    clientes = carregar_clientes()
    if 0 <= cliente_id < len(clientes):
        clientes.pop(cliente_id)
        salvar_clientes(clientes)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)