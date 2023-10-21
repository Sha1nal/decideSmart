from flask_wtf import FlaskForm
from wtforms import import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUp(FlaskForm):
    name = StringField('Name')
    email = EmailField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirmation = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')