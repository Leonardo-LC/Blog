#from app.models import Pessoa


class Cliente:
    def __init__(self, nome, telefone, pets=None):
        self.nome = nome
        self.telefone = telefone
        self.pets = pets if pets is not None else []

    def adicionar_pet(self, nome_pet, tipo_pet):
        self.pets.append({
            'nome': nome_pet,
            'tipo': tipo_pet
        })

    def editar(self, novo_nome, novo_telefone):
        self.nome = novo_nome
        self.telefone = novo_telefone

    def editar_pet(self, pet_index, novo_nome, novo_tipo):
        if 0 <= pet_index < len(self.pets):
            self.pets[pet_index] = {
                'nome': novo_nome,
                'tipo': novo_tipo
            }

    def to_dict(self):
        return {
            'nome': self.nome,
            'telefone': self.telefone,
            'pets': self.pets
        }