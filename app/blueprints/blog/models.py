from app import db
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    blog_user_id = db.Column(db.ForeignKey('blog_user.id'))

    def __repr__(self):
        return f'<BlogPost: {self.id} | {self.body[:10]}...>'

    def from_dict(self, data):
        for field in ['body', 'created_on', 'blog_user_id']:
            if field in data:
                setattr(self, field, data[field])


class BlogUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    posts = db.relationship('BlogPost', backref='user', lazy=True)

    def __repr__(self):
        return f'<BlogUser: {self.id} | {self.email}>'

    def hash_password(self, original_password):
        self.password = generate_password_hash(original_password)

    def check_hashed_password(self, original_password):
        return check_password_hash(self.password, original_password)

    def from_dict(self, data):
        for field in ['first_name', 'last_name', 'email']:
            if field in data:
                setattr(self, field, data[field])