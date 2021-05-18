from app import db
from datetime import datetime as dt
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, index=True)
    last_name = db.Column(db.String, index=True)
    email = db.Column(db.String, index=True, unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }
        return data

    def from_dict(self, data):
        for attr in ['first_name', 'last_name', 'email']:
            if attr in data:
                setattr(self, attr, data[attr])

    def __repr__(self):
        return '<User {}>'.format(self.email)
