from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class FormAluno(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    matricula = IntegerField('matricula', validators=[DataRequired()])
    idade = IntegerField('idade', validators=[DataRequired()])