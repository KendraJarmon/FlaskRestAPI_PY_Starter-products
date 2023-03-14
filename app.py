from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource
from dotenv import load_dotenv
from os import environ

load_dotenv()

# Create App instance
app = Flask(__name__)

# Add DB URI from .env
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')

# Registering App w/ Services
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app)
Migrate(app, db)

# Models
class Products(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    inventory_quantity = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.inventory_quantity} {self.price} {self.description} {self.name}'

# Schemas

class ProductsSchema(ma.Schema):
    class Meta:
        Fields = ('id', 'name', 'description', 'price', 'inventory_quantity')

product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)

# Resources
class ProductListResource(Resource):
    def get():
        return "Hello World"


# Routes
api.add_resource(ProductListResource,)