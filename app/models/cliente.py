
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

    def to_dict(self):
        return {
            'nome': self.nome,
            'telefone': self.telefone,
            'pets': self.pets
        }