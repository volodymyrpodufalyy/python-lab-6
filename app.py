from flask import Flask, request, jsonify
from models.ProductModel import db, ma, Product, product_schema, products_schema
# from controllers import ProductController

# Init app
app = Flask(__name__)

# Init db
db.init_app(app)

# Init ma
ma.init_app(app)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:13247sqlre4lly@localhost/python-lab-6'




