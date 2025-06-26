from datetime import datetime
from app.extensions import db

class Receita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    instrucoes = db.Column(db.Text, nullable=False)
    tempo_preparo = db.Column(db.Integer)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    foto = db.Column(db.String(100))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    ingredientes = db.relationship('Ingrediente', backref='receita', lazy=True)

    def __repr__(self):
        return f"Receita('{self.titulo}', '{self.data_criacao}')"