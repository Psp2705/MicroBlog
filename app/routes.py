from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForms

# @app.route is decorator creates association between URL given as argument and function
# two decorators used associate URLs / and /index to this function 
# web browser requests either of these 2 urls,flask going to invoke 
# this function and pass its return value back to browser as response
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was fantastic!'        
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
# operations that converts complete template into a complete HTML page is called rendering

# to render a template, we use render_template() comes with flask framework


