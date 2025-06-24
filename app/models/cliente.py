from .pessoa import Pessoa  # Import relativo

class Cliente(Pessoa):
    def __init__(self, nome: str, email: str, telefone: str):
        super().__init__(nome, email, telefone)
        self.senha = None
        self.pets = []

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "senha": self.senha,
            "pets": self.pets
        }