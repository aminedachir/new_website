from werkzeug.security import generate_password_hash,check_password_hash
from app import login
from datetime import datetime
from app import db
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#class User(UserMixin, db.Model):
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), unique = True, index = True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120))
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"<User {self.firstname}>"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def _repr__(self):
        return f'Post {self.body}>'