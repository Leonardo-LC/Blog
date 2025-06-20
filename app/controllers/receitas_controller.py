from flask import flash, redirect, url_for
from controllers.upload_controller import save_uploaded_file


def adicionar_receita(request, db, Receitas):
    description = request.form['description']
    descricao = request.form['descricao']

    foto = None
    if 'foto' in request.files:
        file = request.files['foto']
        foto = save_uploaded_file(file)

    receita_existente = Receitas.query.filter_by(description=description).first()
    if receita_existente:
        flash('Erro: Esta receita já foi cadastrada!', 'danger')
        return redirect(url_for('ler_receita'))

    nova_receita = Receitas(
        description=description, #titulo da receita
        descricao=descricao,
        foto=foto
    )

    try:
        db.session.add(nova_receita)
        db.session.commit()
        flash('Receita adicionada com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao adicionar receita: {str(e)}', 'danger')

    return redirect(url_for('ler_receita'))