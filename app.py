# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Listing

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sublet.db'
db.init_app(app)

@app.route('/listings', methods=['GET', 'POST'])
def handle_listings():
    if request.method == 'POST':
        data = request.json
        new_listing = Listing(title=data['title'], description=data['description'], location=data['location'], price=data['price'])
        db.session.add(new_listing)
        db.session.commit()
        return jsonify({'message': 'Listing added'}), 201

    elif request.method == 'GET':
        listings = Listing.query.all()
        return jsonify([{'title': l.title, 'description': l.description, 'location': l.location, 'price': l.price} for l in listings])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
