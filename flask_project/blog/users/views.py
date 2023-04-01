from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required, login_user, logout_user
from blog.app import db
from blog.models import User,Post
from blog.users.forms import RegisterForm, LoginForm, UpdateUserForm
from blog.users.pictures import add_picture

users = Blueprint('users', __name__)

#register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    name = form.name.data,
                    password = form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


#logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))

#login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    if form.validate_on_submit():

        #check if user exists
        #.first() so the query doesn't return a list
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            if user.check_password(form.password.data) and user is not None:
                login_user(user)
                flash('Logged in successfully')

                #get the page the user was trying to access
                next = request.args.get('next')

                if next == None or next[0] != '/':
                    next = url_for('core.index')

                return redirect(next)

    return render_template('login.html', form=form)









