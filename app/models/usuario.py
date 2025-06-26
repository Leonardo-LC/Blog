from app.extensions import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    receitas = db.relationship('Receita', backref='autor', lazy=True)

    def __repr__(self):
        return f"Usuario('{self.nome}', '{self.email}')"