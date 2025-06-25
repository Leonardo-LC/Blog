from flask import Flask, render_template, request, redirect, url_for
from models.cliente import Cliente
import json
import os
from flask import Flask, render_template, request, redirect, url_for
from models.cliente import Cliente
from controllers.cliente_controller import carregar_clientes, salvar_clientes

app = Flask(__name__)
app.secret_key = '123'



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