from app import db, lm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), nullable=False, index=True, unique=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)
    # posts = db.relationship('Post', backref='author', lazy='dynamic')


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 unicode handling
        except NameError:
            return str(self.id)  # python 3 unicode handling

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
