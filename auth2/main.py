from app import app, db
from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required
from models import User
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    return render_template('index.html')

#this is the page that user will be redirected to after logging in
@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

#this is the page that user will be redirected to after logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you logged out")

    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        #checking if user exists
        if user:
            #checking if password is correct
            if user.check_password(form.hashedPW.data):
                login_user(user)
                flash('logged in')

                #redirecting to the page user was trying to access
                next = request.args.get('next')

                #checking if next is not empty and if it starts with /
                if next == None or not next[0] == '/':

                    #if not, redirect to welcome page
                    next = url_for('welcome_user')

                #if correct redirecting to the page user was trying to access
                return redirect(next)

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        #getting our user
        user = User(email=form.email.data, username=form.username.data
                         , hashedPW = form.hashedPW.data)

        #adding user to database
        db.session.add(user)
        db.session.commit()

        flash('Thanks for registering')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)





