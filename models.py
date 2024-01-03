# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Listing {self.title}>'
