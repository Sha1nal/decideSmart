from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, RadioField, StringField, PasswordField, BooleanField, SubmitField, EmailField, TextAreaField, DateTimeField
from wtforms.validators import NumberRange, DataRequired

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    name = StringField('Name')
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirmation = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class DecisionForm(FlaskForm):
    what = TextAreaField('What is the decision you need to make?')
    why = TextAreaField('Why are you making this decision?')
    when = DateField('When does this need to be done?', format='%Y-%m-%d', validators=[DataRequired()])
    impulsive = RadioField('Is this an impulsive decision?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    confident = RadioField('Are you confident about this decision?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    confidence_scale = IntegerField('Scale 1-10', validators=[DataRequired(), NumberRange(min=1, max=10)])
    backup = RadioField('Do you have a backup plan if things dont work out?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    submit = SubmitField('Make Your Decision')