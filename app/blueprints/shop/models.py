from app import db
from datetime import datetime as dt

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Float())
    category_id = db.Column(db.ForeignKey('category.id'))
    tax = db.Column(db.Float())
    description = db.Column(db.Text())
    created_on = db.Column(db.DateTime(), default=dt.utcnow)

    def __repr__(self):
        return f'<Product: {self.name} @{self.price}>'

    def from_dict(self, data):
        for field in ['name', 'price', 'category', 'tax', 'description']:
            if field in data:
                setattr(self, field, data[field])

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    products = db.relationship('Product', cascade='all, delete-orphan', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category: {self.name}>'

    def from_dict(self, data):
        for field in ['name']:
            if field in data:
                setattr(self, field, data[field])