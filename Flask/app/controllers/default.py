from flask import render_template
from app import app, db
from wtforms.ext.appengine.db import model_form
from app.models.forms import FormAluno
from app.models.tables import Aluno

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro_aluno():
    form = FormAluno()
    if form.validate_on_submit():
        a = Aluno(form.nome.data, form.matricula.data, form.idade.data)
        db.session.add(a)
        db.session.commit()
        return "Aluno adicionado com sucesso"
    else:
        print(form.errors)
    return render_template('cadastro.html', form=form)

@app.route("/dashboard")
def dashboard():
    r = Aluno.query.all()
    return render_template('dashboard.html', alunos=r)



@app.route("/teste")
def teste():
    
    #edit
    #r = Aluno.query.filter_by(matricula="32332").first()
    #r.matricula = "21"
    #db.session.add(r)
    #db.session.commit()

    #delete
    #r = Aluno.query.filter_by(matricula="21").first()
    #db.session.delete(r)
    #db.session.commit()
    
    return "OK"