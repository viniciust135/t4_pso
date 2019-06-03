from flask import render_template, request, flash, redirect, url_for
from app import app, db
from wtforms.ext.appengine.db import model_form
from app.models.forms import FormAluno
from app.models.tables import Aluno

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro_aluno():
    form = FormAluno()
    if form.validate_on_submit():
        a = Aluno(form.nome.data, form.matricula.data, form.idade.data)
        db.session.add(a)
        db.session.commit()
        flash("Aluno cadastrado com sucesso", "success")
        return redirect(url_for("dashboard"))
    else:
        print(form.errors)
    return render_template('cadastro.html', form=form)


#editar
@app.route("/editar_aluno/<string:id>", methods=["GET", "POST"])
def editar_aluno(id):
    r = Aluno.query.get(id)
    form = FormAluno()

    form.nome.data = r.nome
    form.matricula.data = r.matricula
    form.idade.data = r.idade

    if form.validate_on_submit():
        r.nome = request.form['nome']
        r.matricula = request.form['matricula']
        r.idade = request.form['idade']
        db.session.add(r)
        db.session.commit()
        flash("Aluno editado com sucesso", "success")
        return redirect(url_for("dashboard"))
    else:
        print(form.errors)
    return render_template('editar_aluno.html', form=form)


#remover
@app.route("/remover_aluno/<string:id>", methods=['POST'])
def remover_aluno(id):
    r = Aluno.query.get(id)
    db.session.delete(r)
    db.session.commit()
    flash("Aluno removido com sucesso", "success")
    return redirect(url_for("dashboard"))


#dashboard
@app.route("/")
@app.route("/dashboard")
def dashboard():
    r = Aluno.query.all()
    return render_template('dashboard.html', alunos=r)