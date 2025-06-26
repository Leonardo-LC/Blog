from ..extensions import db

receita_categoria = db.Table('receita_categoria',
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'), primary_key=True),
    db.Column('categoria_id', db.Integer, db.ForeignKey('categoria.id'), primary_key=True)
)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    receitas = db.relationship('Receita', secondary=receita_categoria, backref=db.backref('categorias', lazy='dynamic'))

    def __repr__(self):
        return f"Categoria('{self.nome}')"