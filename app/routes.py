from flask import render_template, redirect, flash
from app import app
from app.forms import LoginForm, SignUpForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(form.email.data)
        flash(form.name.data)
        flash(form.password.data)
        return redirect('/index')
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(form.email.data)
        flash(form.password.data)
        return redirect('/index')
    return render_template('login.html', form=form)