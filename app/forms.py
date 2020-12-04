from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
    submit = SubmitField('Submit')

class productForm(FlaskForm):
    submit = SubmitField('Submit')

class registerForm(FlaskForm):
    submit = SubmitField('Submit')



