class Animal:
    nome: str
    especie: str
    idade: int
    dono: 'Cliente'  # Agora referencia o objeto Cliente diretamente

    def get_idade_humana(self) -> int:
        """Converte idade animal para equivalente humano"""
        if self.especie.lower() == "cachorro":
            return self.idade * 7
        return self.idade