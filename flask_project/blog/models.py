from blog import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from blog import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User():
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(20), nullable=False,
                              default='default.png')
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, name, email, password_hash):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f"Username {self.name}"


class Post():
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(140))
    text = db.Column(db.Text)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)


    def __init__(self, title, text, topic_id, user_id):
        self.title = title
        self.text = text
        self.topic_id = topic_id
        self.user_id = user_id


    def __repr__(self):
        return f"Post ID: {self.id} --- Date: {self.date} --- Title: {self.title}"



class Topics():
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    topic = db.relationship('Post', backref='topic', lazy='dynamic')

