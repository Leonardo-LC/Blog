from app import create_app
from app.extensions import db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from controllers.upload_controller import allowed_file, save_uploaded_file

app = create_app()

# Importar modelos DEPOIS de criar o app
with app.app_context():
    from models.usuario import Usuario
    from models.receita import Receita
    from models.ingrediente import Ingrediente
    from models.categoria import Categoria

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/receitas')
def listar_receitas():
    receitas = Receita.query.all()
    return render_template('receitas/listar.html', receitas=receitas)


@app.route('/receitas/adicionar', methods=['GET', 'POST'])
def adicionar_receita():
    if request.method == 'POST':
        # Criar receita básica
        nova_receita = Receita(
            titulo=request.form['titulo'],
            instrucoes=request.form['instrucoes'],
            tempo_preparo=request.form['tempo_preparo'],
            usuario_id=1,  # Temporário - substituir por usuário logado
            foto=save_uploaded_file(request.files.get('foto'))
        )

        db.session.add(nova_receita)
        db.session.commit()

        # Adicionar ingredientes
        ingrediente_count = int(request.form.get('ingrediente_count', 1))
        for i in range(ingrediente_count):
            if f'ingredientes[{i}][nome]' in request.form:
                ingrediente = Ingrediente(
                    nome=request.form[f'ingredientes[{i}][nome]'],
                    quantidade=request.form[f'ingredientes[{i}][quantidade]'],
                    unidade=request.form[f'ingredientes[{i}][unidade]'],
                    receita_id=nova_receita.id
                )
                db.session.add(ingrediente)

        # Adicionar categorias
        categorias_selecionadas = request.form.getlist('categorias')
        for cat_id in categorias_selecionadas:
            categoria = Categoria.query.get(cat_id)
            if categoria:
                nova_receita.categorias.append(categoria)

        db.session.commit()
        flash('Receita adicionada com sucesso!', 'success')
        return redirect(url_for('listar_receitas'))

    categorias = Categoria.query.all()
    return render_template('receitas/adicionar.html', categorias=categorias)


# ... (outras rotas CRUD)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)