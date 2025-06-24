class Animal:
    def __init__(self, nome: str, especie: str, idade: int, dono_email: str):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dono_email = dono_email  # Relacionamento com Cliente

    def to_dict(self):
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "dono_email": self.dono_email
        }