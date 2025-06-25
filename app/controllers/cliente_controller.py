import json
import os
from models.cliente import Cliente

DB_FILE = 'clientes_db.json'  # Mantemos a constante aqui

def carregar_clientes():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            dados = json.load(f)
            clientes = []
            for cliente_data in dados:
                cliente = Cliente(
                    nome=cliente_data['nome'],
                    telefone=cliente_data['telefone']
                )
                for pet in cliente_data.get('pets', []):
                    cliente.adicionar_pet(pet['nome'], pet['tipo'])
                clientes.append(cliente)
            return clientes
    return []

def salvar_clientes(clientes):
    with open(DB_FILE, 'w') as f:
        json.dump([cliente.to_dict() for cliente in clientes], f)