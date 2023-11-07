from flask import render_template, redirect, flash
from app import app, db
from app.forms import LoginForm, SignUpForm, DecisionForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Decisions


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect('/index')
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect('/login')
        login_user(user)
        return redirect('/index')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/index')


@app.route('/decision', methods=['GET', 'POST'])
@login_required
def decision(): 
    form = DecisionForm()
    if form.validate_on_submit():
        new_decision = Decisions(user_id=current_user.id, what=form.what.data,
                                 why=form.why.data, when=form.when.data, impulsive=form.impulsive.data, 
                                 confident=form.confident.data, confidence_scale=int(form.confidence_scale.data), 
                                 backup=form.backup.data)
        db.session.add(new_decision)
        db.session.commit()
        return redirect('/index')
    return render_template('decisions.html', form=form)


@app.route('/analytics', methods=['GET', 'POST'])
@login_required
def analytics(): 
    return redirect('/index')


@app.route('/history', methods=['GET', 'POST'])
@login_required
def history(): 
    if current_user.is_authenticated:
        decision_set = current_user.decision.all()
        return render_template('history.html', decision_set=decision_set)