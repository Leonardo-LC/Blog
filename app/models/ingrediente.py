from ..extensions import db

class Ingrediente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.String(50), nullable=False)
    unidade = db.Column(db.String(20), nullable=False)
    receita_id = db.Column(db.Integer, db.ForeignKey('receita.id'), nullable=False)

    def __repr__(self):
        return f"Ingrediente('{self.nome}', '{self.quantidade} {self.unidade}')"