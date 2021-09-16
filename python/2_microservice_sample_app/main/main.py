from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
from dataclasses import dataclass
import requests, json
from producer import publish

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    # Getting some issue when requesting url of admin api to get user id hence hard coding for test purpose
    # req = requests.get('http://docker.for.linux.localhost:8000/api/user') 
    # req = '{"id": 1}'

    # jsonusersdata = json.loads(req)
    jsonusersdata = json.loads('{"id": 1}')
    print(jsonusersdata)

    try:
        print(jsonusersdata)
        productUser = ProductUser(user_id=jsonusersdata['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product liked', id)
    except:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': 'success'
    })
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')