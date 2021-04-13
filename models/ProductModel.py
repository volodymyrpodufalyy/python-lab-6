from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import validate, fields, post_load

# Init db
db = SQLAlchemy()

# Init ma
ma = Marshmallow()


# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# Product Schema
class ProductSchema(ma.Schema):
    id = fields.Int(validate=validate.Range(min=1, max=999))
    name = fields.Str(validate=validate.Length(min=1, max=15))
    description = fields.Str(validate=validate.Length(min=1, max=32))
    price = fields.Float(validate=validate.Range(min=1, max=999))
    quantity = fields.Int(validate=validate.Range(min=1, max=999))

    @post_load
    def make_technique(self, data, **kwargs):
        return Product(**data)


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
