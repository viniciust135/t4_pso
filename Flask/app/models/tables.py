from app import db

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    matricula = db.Column(db.Integer, unique=True)
    idade = db.Column(db.Integer)

    def __init__(self, nome, matricula, idade):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
    
    def __repr__(self):
        return "Nome: %r" % self.nome
