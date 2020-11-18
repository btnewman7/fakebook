from app import db
from datetime import datetime as dt

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    created_on = db.Column(db.DateTime, index=True, default=dt.utcnow)
    user_id = db.Column(db.ForeignKey('user.id'))

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<BlogPost: {self.id} | {self.body[:10]}...>'

    def from_dict(self, data):
        for field in ['body', 'user_id']:
            if field in data:
                setattr(self, field, data[field])