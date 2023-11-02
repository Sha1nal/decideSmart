from flask import render_template, redirect, flash
from app import app
from app.forms import LoginForm, SignUpForm, DecisionForm


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


@app.route('/decision', methods=['GET', 'POST'])
def decision(): 
    form = DecisionForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('decisions.html', form=form)


@app.route('/analytics', methods=['GET', 'POST'])
def analytics(): 
    return redirect('/index')


@app.route('/history', methods=['GET', 'POST'])
def history(): 
    return redirect('/index')