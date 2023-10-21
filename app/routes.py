from flask import render_template
from app import app
from app.forms import LoginForm, SignUpForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)