from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, RadioField, StringField, PasswordField, BooleanField, SubmitField, EmailField, TextAreaField, DateTimeField
from wtforms.validators import AnyOf, ValidationError, NumberRange, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email address already exists')


class DecisionForm(FlaskForm):
    what = TextAreaField('What is the decision you need to make?', validators=[DataRequired()])
    why = TextAreaField('Why are you making this decision?', validators=[DataRequired()])
    when = DateField('When does this need to be done?', format='%Y-%m-%d', validators=[DataRequired()])
    impulsive = RadioField('Is this an impulsive decision?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired(), AnyOf(['yes', 'no'])])
    confident = RadioField('Are you confident about this decision?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired(), AnyOf(['yes', 'no'])])
    confidence_scale = IntegerField('Scale 1-10', validators=[DataRequired(), NumberRange(min=1, max=10)])
    backup = RadioField('Do you have a backup plan if things dont work out?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired(), AnyOf(['yes', 'no'])])
    submit = SubmitField('Make Your Decision')