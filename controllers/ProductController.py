from flask import request, jsonify, abort
from app import app
from marshmallow import ValidationError
from models.ProductModel import db, Product, product_schema, products_schema


@app.errorhandler(404)
def product_not_found(e):
    return '<h1>404 Not Found<h1>\n<p>Resource you requested does not exist.</p>', 404


@app.route('/product', methods=['POST'])
def add_product():
    try:
        new_product = product_schema.load(request.json)
        db.session.add(new_product)
    except ValidationError as err:
        abort(400, err)

    db.session.commit()

    return product_schema.jsonify(request.json)


@app.route('/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)


@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product is None:
        abort(404)
    return product_schema.jsonify(product)


@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if product is None:
        abort(404)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity

    db.session.commit()

    return product_schema.jsonify(product)


@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product is None:
        abort(404)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)
